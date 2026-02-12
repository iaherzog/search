
import matplotlib.pyplot as plt
import folium
from ipywidgets import interact, fixed, IntSlider


def plot_search_step(step_index, history, sbb_data, sbb_graph):
    if not history or step_index >= len(history):
        print("Waiting for search data...")
        return
   
    current, frontier, explored = history[step_index]
    plt.figure(figsize=(10, 7))
    # 1. Set Center and Zoom (not the whole of Switzerland)
    # We center on the initial state provided in the problem [2]
    initial_state = history[0][0] 
    center_x = sbb_data.hubs[initial_state].x
    center_y = sbb_data.hubs[initial_state].y
    
    # Define a focused window around the center (approx. 0.5 degrees)
    plt.xlim(center_y - 0.5, center_y + 0.5)
    plt.ylim(center_x - 0.3, center_x + 0.3)

    # 1. Background: Plot all connections (edges) in light grey
    # This acts as your "map background" [4]
    for start_node, connections in sbb_graph.graph_dict.items():
        x1, y1 = sbb_data.hubs[start_node].x, sbb_data.hubs[start_node].y
        for end_node in connections:
            x2, y2 = sbb_data.hubs[end_node].x, sbb_data.hubs[end_node].y
            plt.plot([y1, y2], [x1, x2], color='lightgrey', linewidth=0.5, zorder=1)

   # 2. Plot Explored Nodes (Blue)
    exp_coords = [[sbb_data.hubs[s].x, sbb_data.hubs[s].y] for s in explored]
    if exp_coords:
        # Extract x and y coordinates correctly
        # Note: Usually, sbb.y (longitude) is the horizontal axis (x) 
        # and sbb.x (latitude) is the vertical axis (y) for maps.
        x_vals = [c[1] for c in exp_coords] # y-coordinates from data
        y_vals = [c[0] for c in exp_coords] # x-coordinates from data
    
        plt.scatter(x_vals, y_vals, color='blue', s=10, label='Explored', zorder=2)

    # 3. Plot Frontier Nodes (Orange)
    front_coords = [[sbb_data.hubs[s].x, sbb_data.hubs[s].y] for s in frontier]
    if front_coords:
        fx_vals = [c[1] for c in front_coords]
        fy_vals = [c[0] for c in front_coords]

        plt.scatter(fx_vals, fy_vals, color='orange', s=15, label='Frontier', zorder=3)
    

    # 4. Plot Current Node (Red)
    curr_x, curr_y = sbb_data.hubs[current].x, sbb_data.hubs[current].y
    plt.scatter([curr_y], [curr_x], color='red', s=50, label='Current', edgecolors='black', zorder=4)

    plt.title(f"Search Step {step_index}: Testing {current}")
    plt.legend()
    plt.axis('off')
    plt.show()


def plot_search_progress(history, sbb_data, sbb_graph):
    if len(history) > 0:
        interact(plot_search_step, 
                step_index=IntSlider(min=0, max=len(history)-1, step=1, value=0),
                history=fixed(history), 
                sbb_data=fixed(sbb_data), 
                sbb_graph=fixed(sbb_graph))
    else:
        print("Search history is empty. Check your initial state and Goal Test.")

def create_map(sbb):
    map_ch = folium.Map(location=[46.8, 8.33],
                    zoom_start=8)

    for hub in sbb.hubs:
        folium.CircleMarker(location=[sbb.hubs[hub].x, sbb.hubs[hub].y],
                            radius=2,
                            weight=4).add_to(map_ch)
    return map_ch


def add_solution_to_map( goal_node, sbb_data, map):

    points = []

    for hub in goal_node.get_path_from_root():
        points.append([sbb_data.hubs[hub.state].x, sbb_data.hubs[hub.state].y])
        folium.CircleMarker(location=[sbb_data.hubs[hub.state].x, sbb_data.hubs[hub.state].y], color='red',
                        radius=2,
                        weight=4).add_to(map)
    folium.PolyLine(points, color='red').add_to(map)
    return map

def create_tsp_map(path, sbb):

    map = folium.Map(location=[46.8, 8.33],
                    zoom_start=8)
    points = []
    first_city = path[0]
    for city in path:
        points.append([sbb.hubs[city].x, sbb.hubs[city].y])
        folium.Marker([sbb.hubs[city].x, sbb.hubs[city].y], popup=city).add_to(map)
    points.append([sbb.hubs[first_city].x, sbb.hubs[first_city].y])   
    folium.PolyLine(points, color='red').add_to(map)
    return map