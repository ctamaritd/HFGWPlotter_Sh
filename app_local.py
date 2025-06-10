#HGSapp.py

# Import all the relevant libraries and packages


from aux.imports import *


from aux.data_files import detector_data
from aux.aux_functions import load_and_categorize_data
from aux.aux_functions import create_sliders
from aux.aux_functions import create_curves_dict
from aux.aux_functions import add_curves_to_plot

# Create a Blueprint
Shplot = Blueprint('Shplot', __name__, static_folder='Shplot/static', template_folder='Shplot/templates')











# Suppress specific Bokeh warning
warnings.filterwarnings("ignore", message="ColumnDataSource's columns must be of the same length")






# Create a Flask app and register the Blueprint with a URL prefix
app = Flask(__name__)
app.secret_key = 'NotSoSecretKey'
UPLOAD_FOLDER = '/tmp/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


## Load detector curves

# Load data into Data class instances collected in the dictionary data_instances
# Create a dictionary category_dict containing the experiment labels divided into categories (Indirect bounds, Direct bounds, Projected bounds and others)
data_instances, physics_category_dict, curve_category_dict = load_and_categorize_data(detector_data)
## Define app section



@Shplot.before_request
def assign_user_id():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())

@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')


@Shplot.route('/get_comments')
def get_comments():
    label = request.args.get('label')
    data_instance = data_instances.get(label, None)
    comment = data_instance.comment if data_instance and data_instance.comment not in [None, ''] else None

    return jsonify({'comment': comment})



@Shplot.route('/upload', methods=['POST'])
def upload():
    file = request.files['csvfile']
    if file and file.filename.endswith('.csv'):
        user_id = session.get("user_id")
        path = os.path.join(UPLOAD_FOLDER, f"{user_id}.csv")
        file.save(path)
    return '', 204  # No Content; prevents browser refresh



# Flask route to serve the HTML template with the initial Bokeh plot
@Shplot.route('/')
def index():
    session_id = session.get("user_id")
    script_bokeh_plot = server_document(url=f"http://localhost:5006/Shplotworkers/plot", arguments={"session_id": session_id})


    return render_template(
        'index.html',
        script_bokeh_plot = script_bokeh_plot,
        bokeh_css=INLINE.render_css(),
        bokeh_js=INLINE.render_js(),
        physics_category_dict= physics_category_dict,
        curve_category_dict= curve_category_dict
    )



#Bokeh app for all
def bokeh_plot_app(doc):
    args = doc.session_context.request.arguments
    #print("ARGS:", args)
    session_id = args.get("session_id", [b"default"])[0].decode()
    csv_path = os.path.join(UPLOAD_FOLDER, f"{session_id}.csv")
    #print(f"[DEBUG] session_id from server_document: {session_id}")
    print(f'csv_path: {csv_path}')
    last_modified = None  # Track the last file change time

    #Start assuming no uploaded file by user


    #Global variables that can be seen by all users, even if they are fed different plots
    #global  data_instances, physics_category_dict, curves_category_dict, curves_dict






    # Global ColumnDataSource objects to manage plot data



    plot_source_rectangles = ColumnDataSource(data=dict(), name='plot_source_rectangles')
    plot_source_curves = ColumnDataSource(data=dict(), name='plot_source_curves')
    plot_source_areas = ColumnDataSource(data=dict(), name='plot_source_areas')
    plot_source_lollipops = ColumnDataSource(data=dict(), name='plot_source_lollipops')
    # Annotations object
    annotation_source = ColumnDataSource(data=dict(), name='annotation_source')



    # Set up the figure

    #Global parameters for range, width and height


    #Shmin = 10.**-40
    #Shmax = 10.**-19
    #hmin = 10.**-39.
    #hmax = 10.**-10.

    #Fig 1
    Shmin = 10**-25.5
    Shmax = 10**-15.5
    fmin = 1e1
    fmax = 1e11

    #Higher freq plot
    #Shmin = 10**-40.5
    #Shmax = 10**-19
    #fmin = 10**10.
    #fmax = 10**19.

    #Interf.  plot
    #Shmin = 10**-26
    #Shmax = 10**-15.5
    #fmin = 10**1.5
    #fmax = 10**8.5

    #Modern res mass det  plot
    #Shmin = 10**-25.5
    #Shmax = 10**-15.5
    #fmin = 10**1.5
    #fmax = 10**9

    #Photon reg. plot
    #Shmin = 10**-41
    #Shmax = 10**-16
    #fmin = 10**8
    #fmax = 10**19


    #EM oscillators plot
    #Shmin = 10**-25
    #Shmax = 10**-15.5
    #fmin = 10**4.5
    #fmax = 10**11


    Shrangechanged = 0


    frangechanged = 0
    plot_width = int(900)
    plot_width_changed = 0
    plot_height = 600 #(added 80 points for the legend height: 3itmes*(20 glyph+10 padding)+2*(10padding))
    legend_height = 0
    plot_height_changed = 0
    xrange = (fmin, fmax)
    yrange = (Shmin, Shmax)
    #custom_major_ticker = LogTicker(base=10, min_interval=1, num_minor_ticks=10)  # Major ticks at each decade
    #custom_minor_ticker = LogTicker(base=10, mantissas=[2, 3, 4, 5, 6, 7, 8, 9])  # Minor ticks


    fig = figure(background_fill_color='white',
    border_fill_color='black',
    border_fill_alpha=0.0,
    height= plot_height,
    width= plot_width,
    x_axis_label=r'GW frequency $$f\,\,[{\rm Hz}]$$',
    x_axis_type='log',
    x_axis_location='below',
    x_range=xrange,
    y_axis_label=r'noise-equivalent strain PSD $$\left(S_h^{\rm noise}\right)^{1/2} [{\rm Hz}^{-1/2}]$$',
    y_axis_type='log',
    y_axis_location='left',
    y_range=yrange,
    toolbar_location='below',
    tools='save',name = 'myplot')
    #fig.output_backend = "svg"
    fig.xgrid.level = 'image'
    fig.ygrid.level = 'image'
    # Add an extra logarithmic axis on the top
    log_axis_top = LogAxis()
    fig.add_layout(log_axis_top, 'above')

    # Add an extra logarithmic axis on the right
    log_axis_right = LogAxis()
    fig.add_layout(log_axis_right, 'right')


    custom_ticks_xaxis= [10**i for i in range(-19,21)]
    custom_ticks_yaxis= [10**i for i in range(-40,1)]
    custom_ticks_minor_xaxis = [j * 10**i for i in range(-19, 21) for j in range(2,10)]
    custom_ticks_minor_yaxis = [j * 10**i for i in range(-41, 1) for j in range(2,10)]
    fig.xaxis.ticker = FixedTicker(ticks=custom_ticks_xaxis, minor_ticks=custom_ticks_minor_xaxis)
    fig.yaxis.ticker = FixedTicker(ticks=custom_ticks_yaxis, minor_ticks=custom_ticks_minor_yaxis)

    # Customize tick label sizes
    fig.xaxis.major_label_text_font_size = "12pt"  # Change x-axis tick label size
    fig.yaxis.major_label_text_font_size = "12pt"  # Change y-axis tick label size

    fig.xaxis.axis_label_text_font_size = "12pt"  # Change x-axis label size
    fig.yaxis.axis_label_text_font_size = "12pt"  # Change y-axis label size
    #fig.title.title_text_font_size = "12pt"  # Change y-axis label size

    #Label right-down corner
    watermark = Label(x=fig.width - 285, y=15, x_units = 'screen', y_units = 'screen', text=r"HFGWPlotter",  text_font_size="12pt", text_color="gray", text_font_style="bold", background_fill_color="white",background_fill_alpha=0.7, name = "watermark")
    #Label upper right
    #label = Label(x=585, y=450, x_units = 'screen', y_units = 'screen', text=r"Aggarwal et al. 2025",  text_font_size="12pt", text_color="gray", text_font_style="bold", background_fill_color="white",
    #background_fill_alpha=1)
    # Add the Label to the plot
    fig.add_layout(watermark)
    #fig.log_axis_top.ticker = FixedTicker(ticks=custom_ticks_xaxis)
    #fig.xaxis.ticker.num_minor_ticks = 10

    #fig.title = Title(text=r"$$\text{Photon (re)generation experiments}$$", text_font_size="12pt", align="center")




    # Set up the sliders

    slider_x, slider_y, slider_width,  slider_height, user_color_picker, user_label_input, user_label_size, user_label_x, user_label_y, user_label_angle = create_sliders(fig, Shmin, Shmax)


    # Create dictionary of curves

    curves_dict = create_curves_dict(data_instances, physics_category_dict, curve_category_dict)

    # Link curves to a chart
    fig, plot_source_rectangles,  plot_source_curves, plot_source_areas, plot_source_lollipops,  annotation_source = add_curves_to_plot(fig, curves_dict, physics_category_dict, curve_category_dict,  plot_source_rectangles, plot_source_curves, plot_source_areas, plot_source_lollipops, annotation_source)



    #Add legend at this stage
    # Retrieve renderers by their name
    renderer_current = fig.select(name="LIGO")
    renderer_ongoing = fig.select(name="DMRadio-GUT")
    renderer_ongoing_res = fig.select(name="DMRadio-GUT-res")
    renderer_proposed =  fig.select(name="Mag. Weber bars")
    renderer_proposed_res =  fig.select(name="Mag. Weber bars (res)")


    # Add a dummy glyph for intermediate text
    dummy_line = fig.line([], [], line_alpha=0)  # Invisible line for the "header"
    # Create a custom legend
    legend = Legend(items=[
        (r"Current", [renderer_current[0]]),  # Access the first matching renderer
        (r"In development (solid: broad, dotted: res.)", [renderer_ongoing[0],renderer_ongoing_res[0]]),
        (r"Proposed (solid: broad, dotted: res.)", [renderer_proposed[0],renderer_proposed_res[0]]),
    ],
    glyph_height=20,  # Glyph height in points
    glyph_width=20,   # Glyph width in points
    spacing=-1,       # Spacing between items in points
    padding=100        # Padding inside the legend box in points
    )
    # Customize the font size of the legend labels
    legend.label_text_font_size = "11pt"  # Set the font size for the legend labels
    legend.location = (10, 10)  # Custom (x, y) position in plot space
    legend.border_line_color = None  # Hide the frame
    legend.background_fill_alpha = 0.5  # Set background transparency (50%)
    # Add the legend to the figure
    fig.add_layout(legend, 'center')
    # Create a separate figure to hold the legend
    #legend_fig = figure(height=200, width=400, toolbar_location=None, outline_line_color=None)

    # Add dummy glyphs to represent legend items
    #line_ongoing_dummy = legend_fig.line([0,1], [0,1], line_width=2, color="rebeccapurple", visible = False)  # Same style as in the main plot
    #line_proposed_dummy = legend_fig.line([0,1], [0,1], line_width=2, color="darkcyan", visible = False)
    #Dummy glyph for area
    #area_current_dummy =legend_fig.patch(
    #x=[0, 1, 1, 0],  # Example rectangle coordinates
    #y=[0, 0, 1, 1],
    #fill_color="darkorange",
    #fill_alpha=0.4,
    #line_color=None, visible = False # Match style of the area plot
    #)

    # Create a custom legend
    #legend = Legend(items=[
    #    ("Current bounds", [area_current_dummy]),  # Access the first matching renderer
    #    ("Experiments in active development", [line_ongoing_dummy]),
    #    ("Proposed experiments", [line_proposed_dummy])
    #])

    # Remove axes, gridlines, and other visuals from the dummy figure
    #legend_fig.xaxis.visible = False
    #legend_fig.yaxis.visible = False
    #legend_fig.grid.visible = False
    #legend_fig.outline_line_color = None

    #legend_fig.add_layout(legend, 'center')





    #Main plot with range/size sliders
    layout = column(fig)
    #Sliders for range/size
    layout_size = column(Div(text="<h1>Plot range and size</h1>"), slider_x, slider_y,   slider_width, slider_height)
    layout_user = column(Div(text="<h1>Customize your curve</h1>"), user_color_picker, user_label_input, user_label_size, user_label_x, user_label_y, user_label_angle,  visible = False, name = "panel2_Your curve")




    #Function that updates annotation_angles and positions
    def update_annotation_angles(curves_dict,  annotation_source, fig, fmin, fmax, Shmin, Shmax):

        nonlocal user_label_angle
        # To reduce individual changes (communications with server) update main variable only once, so we use first copy
        new_data_annotation = dict(annotation_source.data)

        curves_dict_to_use = curves_dict


        #Update plot_sources

        for label, data in curves_dict_to_use.items():
            # Generate keys for delta_x and delta_y dynamically based on the label
            annotation_x_key = f'annotation_x_{label}'  # Adjusted to use the dynamic key
            annotation_y_key = f'annotation_y_{label}'  # Adjusted to use the dynamic key
            label_angle_key  = f'label_angle_{label}'

            x_label = data.get(annotation_x_key, 0)
            y_label = data.get(annotation_y_key, 0)

            new_data_annotation[annotation_x_key] = [x_label]  # Change the x position
            new_data_annotation[annotation_y_key] = [y_label]  # Change the x position


            #Change label angles for selected curves when going from hc to Omega
            label_angle = data.get(label_angle_key, 0)


            ratio = ((np.log10(Shmax)-np.log10(Shmin))/(np.log10(fmax)-np.log10(fmin)))*fig.width/(fig.height-legend_height)#subtract height 110 of legend
            new_label_angle = np.arctan(1/ratio*(np.tan(label_angle)))#np.arctan(1/ratio*(2.*np.tan(label_angle)-1))
            new_data_annotation[label_angle_key] = [new_label_angle]
            #For user curve, change slider position
            if label == 'Your curve':
                user_label_angle.value = new_label_angle



        return new_data_annotation


    #Define a callback function for plot size, and update annotation angles, for example after changing range which affects aspect ratio
    def update_frange(new, curves_dict):

        nonlocal fig
        nonlocal annotation_source
        nonlocal fmin
        nonlocal fmax

        fmin = 10.**new[0]
        fmax = 10.**new[1]
        fig.x_range.start  = fmin
        fig.x_range.end = fmax

        annotation_source.data = update_annotation_angles(curves_dict, annotation_source, fig, fmin, fmax, Shmin, Shmax)


    slider_x.on_change('value', lambda attr, old, new: update_frange(new, curves_dict))

    def update_Shrange(new, curves_dict):

        nonlocal fig
        nonlocal annotation_source
        nonlocal Shmin
        nonlocal Shmax



        Shmin = 10.**new[0]
        Shmax = 10.**new[1]

        fig.y_range.start = Shmin
        fig.y_range.end = Shmax

        annotation_source.data =  update_annotation_angles(curves_dict, annotation_source, fig, fmin, fmax, Shmin, Shmax)


    slider_y.on_change('value', lambda attr, old, new: update_Shrange(new, curves_dict))



    def update_width(new, curves_dict):

        nonlocal fig
        nonlocal annotation_source
        nonlocal watermark

        new_width = slider_width.value
        fig.width = new_width;

        watermark.x = new_width-285;



        annotation_source.data =  update_annotation_angles(curves_dict,  annotation_source, fig, fmin, fmax, Shmin, Shmax)



    slider_width.on_change('value', lambda attr, old, new: update_width(new, curves_dict))


    def update_height(new, curves_dict):

        nonlocal fig
        nonlocal annotation_source

        fig.height = slider_height.value;
        annotation_source.data =  update_annotation_angles(curves_dict,  annotation_source, fig, fmin, fmax, Shmin, Shmax)

    slider_height.on_change('value',  lambda attr, old, new: update_height(new, curves_dict))

    ##################################################
    ##################################################
    ##################################################
    #update user curve

    def update_user_color(attr, old, new):
        nonlocal annotation_source
        label = 'Your curve'
        line = fig.select(name=label)[0]  # get first match
        line.glyph.line_color = new

        new_data_annotation = dict(annotation_source.data)
        label = 'Your curve'
        label_color_key = f'label_color_{label}'

        new_data_annotation[label_color_key ] = [new]  # Change the x position
        annotation_source.data = new_data_annotation

        #labelset = fig.select(name=f'annotation_{label}')[0]  # Get LabelSet by name
        #labelset.text_color = new


    user_color_picker.on_change('color', update_user_color)

    def update_user_label(new):
        nonlocal annotation_source
        ## To reduce individual changes (communications with server) update main variable only once, so we use first copy
        new_data_annotation = dict(annotation_source.data)
        label = 'Your curve'
        label_text_key = f'annotation_text_{label}'

        new_data_annotation[label_text_key] = [new]  # Change the x position
        annotation_source.data = new_data_annotation


    user_label_input.on_change('value',  lambda attr, old, new: update_user_label(new))

    def update_user_label_size(new):
        nonlocal annotation_source
        ## To reduce individual changes (communications with server) update main variable only once, so we use first copy
        new_data_annotation = dict(annotation_source.data)
        label = 'Your curve'
        label_size_key = f'label_size_{label}'

        new_data_annotation[label_size_key] = [new]  # Change the x position
        annotation_source.data = new_data_annotation


    user_label_size.on_change('value',  lambda attr, old, new: update_user_label_size(new))

    def update_user_label_x(new):
        nonlocal annotation_source
        nonlocal curves_dict

        label = 'Your curve'
        annotation_x_key = f'annotation_x_{label}'  # Adjusted to use the dynamic key
        #Update curves dict (necessary for jumps between h2Omega and hc)
        curves_dict[label][annotation_x_key] = 10.**new

        ## To reduce individual changes (communications with server) update main variable only once, so we use first copy
        new_data_annotation = dict(annotation_source.data)

        new_data_annotation[annotation_x_key] = [10.**new]  # Change the x position
        annotation_source.data = new_data_annotation

    user_label_x.on_change('value',  lambda attr, old, new: update_user_label_x(new))

    def update_user_label_y(new):
        nonlocal annotation_source
        nonlocal curves_dict
        label = 'Your curve'

        annotation_y_key = f'annotation_y_{label}'  # Adjusted to use the dynamic key
        annotation_y_aux = 10.**new

        curves_dict[label][annotation_y_key] = annotation_y_aux

        ## To reduce individual changes (communications with server) update main variable only once, so we use first copy
        new_data_annotation = dict(annotation_source.data)


        new_data_annotation[annotation_y_key] = [10.**new]  # Change the y position
        annotation_source.data = new_data_annotation

    user_label_y.on_change('value',  lambda attr, old, new: update_user_label_y(new))

    def update_user_label_angle(new):
        nonlocal annotation_source
        nonlocal curves_dict

        nonlocal fmin, fmax, Shmin, Shmax
        label = 'Your curve'
        label_angle_key  = f'label_angle_{label}'

        ## To reduce individual changes (communications with server) update main variable only once, so we use first copy
        new_data_annotation = dict(annotation_source.data)
        new_data_annotation[label_angle_key] = [new]  # Change the Angle directly in annotation

        #Save angle to dictionary (needed for change between hc/h2Omega), correct for ratio
        #Angle is not changed between dictionaries
        ratio = ((np.log10(Shmax)-np.log10(Shmin))/(np.log10(fmax)-np.log10(fmin)))*fig.width/(fig.height-legend_height)
        new_label_angle_dict = np.arctan(1/ratio*(np.tan(new)))

        curves_dict[label][label_angle_key] = new_label_angle_dict


        annotation_source.data = new_data_annotation

    user_label_angle.on_change('value',  lambda attr, old, new: update_user_label_angle(new))
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #Update plot when external csv loaded
    def update_from_external_csv():

        nonlocal plot_source_curves
        nonlocal curves_dict
        nonlocal last_modified

        if os.path.exists(csv_path):
            stat = os.stat(csv_path)
            if last_modified is None or stat.st_mtime > last_modified:
                    last_modified = stat.st_mtime
                    print("Reloading file:", csv_path)
                    try:
                        #print('recognized not loaded, os.path.exists')
                        df = pd.read_csv(csv_path,  header=None, names=['x', 'y'])


                        if 'x' in df.columns and 'y' in df.columns:
                            #new_data_curves[x_key] = df['x']
                            #new_data_curves[y_key] = df['y']
                            xuser = df['x']
                            yuser = df['y']
                            lenCSV = len(xuser)
                            label = 'Your curve'
                            lenDict = len(curves_dict[label][f'xCurve_{label}'])
                            #If length of CSV < current max length, just refill user data
                            if lenDict >= lenCSV:
                                nextra = lenDict - lenCSV
                                x_key = f'xCurve_{label}'
                                y_key = f'yCurve_{label}'
                                if nextra > 0:
                                    xextra = np.array([ xuser[lenCSV-1] for _ in range(nextra) ])
                                    yextra = np.array([ yuser[lenCSV-1] for _ in range(nextra) ])
                                    xuser = np.concatenate([xuser,xextra])
                                    yuser = np.concatenate([yuser,yextra])
                                #Update curves dict. Assume data is for h2Omega
                                curves_dict[label][x_key] = xuser
                                curves_dict[label][y_key] = yuser
                                #If we are plotting h2Omega, update source
                                plot_source_curves.data[x_key] = xuser
                                plot_source_curves.data[y_key] = yuser
                            #If length of CSV > current max length, need to refill all other curves in "Curves" category
                            #To avoid too many calls to change plot_source_curves, we use dict new_data_curves and update source in the end
                            else:
                                new_data_curves = {}
                                nextra =  lenCSV - lenDict
                                for label, data in curves_dict.items():
                                    # Determine the category of the curve
                                    category = None
                                    for cat, labels in curve_category_dict.items():
                                        if label in labels:
                                            category = cat
                                            break
                                    if category == 'Curves':
                                        if 'Your curve' not in label:
                                            x_key = f'xCurve_{label}'
                                            y_key = f'yCurve_{label}'
                                            ###Read curves dict and modify
                                            xaux = data[x_key]
                                            yaux = data[y_key]
                                            #print(f'{label}: xaux: {xaux}')
                                            #print(f'{label}: yaux: {yaux}')
                                            xextra = np.array([ xaux[lenDict-1] for _ in range(nextra) ])
                                            yextra = np.array([ yaux[lenDict-1] for _ in range(nextra) ])
                                            xaux = np.concatenate([xaux,xextra])
                                            yaux = np.concatenate([yaux,yextra])
                                            curves_dict[label][x_key] = xaux
                                            curves_dict[label][y_key] = yaux
                                            #If we are plotting h2Omega, update new data
                                            new_data_curves[x_key] = xaux
                                            new_data_curves[y_key] = yaux
                                        if label == 'Your curve': #Now we are in user data, no need to concatenate
                                            x_key = f'xCurve_{label}'
                                            y_key = f'yCurve_{label}'
                                            #Update curves dict.
                                            curves_dict[label][x_key] = xuser
                                            curves_dict[label][y_key] = yuser
                                            new_data_curves[x_key] =  xuser
                                            new_data_curves[y_key] =  yuser

                                plot_source_curves.data = new_data_curves


                            #We use this method to only have one call to change plot_source (as opposed to changing x and changing y with 2 statments)
                            #plot_source_curves.data = new_data_curves
                            print(f"CSV loaded for session {session_id}")
                    except Exception as e:
                        print(f"Error reading CSV: {e}")


    # Check every 2 seconds
    doc.add_periodic_callback(update_from_external_csv, 2000)

    def cleanup_session(session_context):
        try:
            if os.path.exists(csv_path):
                os.remove(csv_path)
                print(f"[CLEANUP] Removed file for session {session_id}")
        except Exception as e:
            print(f"[ERROR] Failed to delete file for session {session_id}: {e}")

    doc.on_session_destroyed(cleanup_session)





    # Add the layout to the Bokeh document
    final_layout = column(layout,  Div(text="<div style='height: 10px; background-color: black; width: 100%;'></div>"), row(layout_size,Div(text="<div style='width: 10px; background-color: black; height: 100%;'></div>"),  Div(text="<div style='width: 10px; background-color: black; height: 100%;'></div>"), layout_user), sizing_mode="scale_both")
    doc.add_root(final_layout)



plot_app = Application(FunctionHandler(bokeh_plot_app))





app.register_blueprint(Shplot, url_prefix='/Shplot')


###########################################
##CODE TO RUN WITH FLASK INTEGRATED SERVER
###########################################
# Start Flask app in a separate thread
flask_thread = Thread(target=lambda: app.run(debug=True, port=5003, use_reloader=False))
flask_thread.start()

# Create and start a single Bokeh server with the different apps with different urls
server = Server({'/plot': plot_app}, prefix="/Shplotworkers", io_loop=IOLoop.current(), allow_websocket_origin=["*","localhost:5006","127.0.0.1:5006","localhost:5003","127.0.0.1:5003"], port=5006)
server.start()



if __name__ == '__main__':
     server.io_loop.start()
     flask_thread.join()

