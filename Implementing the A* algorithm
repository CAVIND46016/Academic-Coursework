# Write a python program called \q1.py" that accepts as an argument 
# an input file containing the locations of the cities and highways, a starting city and a destination city.
# Your program should output the length of the shortest path between the starting city and
# the destination. If no path exists it should output \NO PATH EXISTS".
# You should use the A* algorithm with any non-trivial admissible heuristic of your choice.

import yaml
import sys
import math

def yaml_Loader():
#     yaml_input_file = open(sys.argv[1], 'r');
    yaml_input_file = open("sample-input.yaml", 'r');
    # 'Try', 'Except' logic used from '//http://pyyaml.org/wiki/PyYAMLDocumentation'.
    try:
        data = yaml.load(yaml_input_file);
    except (yaml.YAMLError, exc):
        print ("Error in configuration file:", exc);
        
    yaml_input_file.close();  
    return data;

#Euclidean Heuristic used.
def euclideanDistance(_A, _B):
    return (math.sqrt((_A[0] - _B[0])**2 + (_A[1] - _B[1])**2));

def main():
    data = yaml_Loader();
    
    dict_cities = data.get('cities');
    highways    = data.get('highways');
         
    startState  = data.get('start');
    goalState   = data.get('end');
    
    frontier    = [startState]; 
    # f = g + h = 0 for the initial state.
    f_cost      = [0]; 
    g_cost      = [0];
    exploredSet = [];
    
    pathExists = False;
    for loc1, loc2 in highways:
        if((loc1 == goalState or loc2 == goalState)):
            pathExists = True;
                          
    if(pathExists == False):
        print("NO PATH EXISTS.")
    else:        
        while(frontier != []): 
            if(frontier[0] == goalState): # Goal state found
                exploredSet.append(goalState);
                break;  
        
            for loc1, loc2 in highways:
                if(loc1 == frontier[0] or loc2 == frontier[0]):
                
                    if(loc1 == frontier[0]):
                        g_tmp   = g_cost[0] + euclideanDistance(dict_cities[loc1], dict_cities[loc2]);
                        h_tmp   = euclideanDistance(dict_cities[loc2], dict_cities[goalState]);
                        frontier.append(loc2);
                    else:
                        g_tmp   = g_cost[0] + euclideanDistance(dict_cities[loc2], dict_cities[loc1]);
                        h_tmp   = euclideanDistance(dict_cities[loc1], dict_cities[goalState]);
                        frontier.append(loc1);
                        
                    g_cost.append(g_tmp);
                    f_cost.append(g_tmp + h_tmp);
                
            exploredSet.append(frontier[0]);
            frontier.pop(0);
            g_cost.pop(0);
            f_cost.pop(0);
            
            for index, item in enumerate(f_cost):
                if (item == min(f_cost)):
                    tmp = frontier[0];
                    frontier[0] = frontier[index];
                    frontier[index] = tmp;
                    
                    tmp = g_cost[0];
                    g_cost[0] = g_cost[index];
                    g_cost[index] = tmp;
                    
                    tmp = f_cost[0];
                    f_cost[0] = f_cost[index];
                    f_cost[index] = tmp;
                    
    if(pathExists == True):               
        print(f_cost[0]);
        
if __name__ == "__main__":
    main();
