# Agents and Environments

def check_environment_logic(student_dict):
    # Defining the correct properties based on the search problem model 
    expected = {
        "observable": "fully", 
        "predictability": "deterministic", 
        "persistence": "static", 
        "parameters": "discrete",
        "time_dependency": "sequential",
        "knowledge": "known",
        "agents": "single"
    }
    
    hints = {
        "observable": "Does the agent have access to the complete map data?",
        "predictability": "Do actions always achieve the desired effect in our search graph?",
        "persistence": "Does the SBB map change while the algorithm is searching?",
        "parameters": "Is there a finite set of stations and connections?",
        "time_dependency": "Do current choices affect which future paths are available? ",
        "knowledge": "Does the agent already know all the stations and connections?",
        "agents": "Is there another rational entity that needs to be considered by our agent?"
    }

    

    for key, correct_val in expected.items():
        student_val = student_dict.get(key).lower()
        if student_val is None:
            print(f"❌ {key.replace('_', ' ').capitalize()}: No answer provided.")
            continue
        if student_val == correct_val:
            print(f"✅ {key.capitalize()}: Correct!")
        else:
            print(f"❌ {key.replace('_', ' ').capitalize()}: Not quite. Hint: {hints[key]}")

## Agent Type
def check_number_of_entries_at_t3(student_value):
    correct_value = 64 
    if student_value == correct_value:
        print("✅ Number of entries at t=3: Correct!")
    else:
        print(f"❌ Number of entries at t=3: Incorrect. ")

def check_total_number_of_entries_for_three_steps(student_value):
    correct_value = 84 
    if student_value == correct_value:
        print("✅ Total number of entries for  t=3: Correct!")
    else:
        print(f"❌ Total number of entries after t=3: Incorrect.")

def check_student_function(student_function):

    try:
        assert student_function(4,1) == 4,  "Wrong result for 4 percepts and lifetime 1"
        assert student_function(4,2) == 20, "Wrong result for 4 percepts and lifetime 2"
        assert student_function(4,3) == 84, "Wrong result for 4 percepts and lifetime 3"

        print("✅ Student function: Correct implementation!")
    except Exception as e:
        print(f"❌ Student function is incorrect. Error: {e}")     

## Modeling Search Problems

def test_connected_cities_of_arad(value):
    correct_value = {'Zerind', 'Sibiu', 'Timisoara'}
    if value == correct_value:
        print("✅ Connected cities of Arad: Correct!")
    else:
        print(f"❌ Connected cities of Arad: Incorrect. Expected: {correct_value}, but got: {value}")


def test_distance_arad_timisoara(value):
    correct_value = 118
    if value == correct_value:
        print("✅ Distance between Arad and Timisoara: Correct!")
    else:
        print(f"❌ Distance between Arad and Timisoara: Incorrect. Expected: {correct_value}, but got: {value}")


def test_actions_in_arad(value):
    correct_value = ['Zerind', 'Sibiu', 'Timisoara']
    if set(value) == set(correct_value):
        print("✅ Actions in Arad: Correct!")
    else:
        print(f"❌ Actions in Arad: Incorrect. Expected: {correct_value}, but got: {value}")


def test_cost_arad_to_zerind(value):
    correct_value = 75
    if value == correct_value:
        print("✅ Cost from Arad to Zerind: Correct!")
    else:
        print(f"❌ Cost from Arad to Zerind: Incorrect. Expected: {correct_value}, but got: {value}")


        # --- Node Class Sanity Check ---
def test_node_implementation(Node):    
    try:
        # 1. Test Root Node (Initial State)
        test_state_root = 'Arad'
        root_node = Node(state=test_state_root)
        
        # Check attributes exist
        assert hasattr(root_node, 'state'), "Node is missing the 'state' attribute." [3]
        assert hasattr(root_node, 'parent'), "Node is missing the 'parent' attribute." [1]
        assert hasattr(root_node, 'action'), "Node is missing the 'action' attribute." [1]
        
        # Check correct values for root
        assert root_node.state == test_state_root, f"Expected state '{test_state_root}', but got '{root_node.state}'."
        assert root_node.parent is None, "The root node's parent should be None." [1]
        assert root_node.action is None, "The root node's action should be None." [1]
        
        # 2. Test Child Node (Successor State)
        test_state_child = 'Sibiu'
        test_action = 'Sibiu'
        child_node = Node(state=test_state_child, parent=root_node, action=test_action, path_cost=140)
        
        # Check attribute linking
        assert child_node.parent == root_node, "The child node's parent is not linked correctly."
        assert child_node.action == test_action, f"Expected action '{test_action}', but got '{child_node.action}'."
        
        # 3. Test Path Cost and Depth (as seen in lecture slides)
        if hasattr(child_node, 'path_cost'):
            assert child_node.path_cost == 140, "Path cost not assigned correctly." 
        
        # If you implemented depth logic
        if hasattr(child_node, 'depth'):
            assert root_node.depth == 0, "Root node depth should be 0." 
            assert child_node.depth == 1, "Child node depth should be parent.depth + 1." 

        print("✅ Node Sanity Check Passed: All required attributes are present and correctly assigned!")

    except AssertionError as e:
        print(f"❌ Sanity Check Failed: {e}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

def test_initial_state(value):

    if value == 'Arad':
        print("✅ Innitial state: Correct!")
    else:
        print(f"❌ Initial state: Incorrect. Expected: Arad, but got: {value}")

def test_children_of_initial_node(children):
    expected_children_states = {'Zerind', 'Sibiu', 'Timisoara'}
    actual_children_states = {child.state for child in children}
    if actual_children_states == expected_children_states:
        print("✅ Children of initial node: Correct!")
    else:
        print(f"❌ Children of initial node: Incorrect. Expected: {expected_children_states}, but got: {actual_children_states}")

def test_next_node_state(value):
    if value == 'Sibiu':
        print("✅ Next node state after action 'Sibiu': Correct!")
    else:
        print(f"❌ Next node state after action 'Sibiu': Incorrect. Expected: Sibiu, but got: {value}")