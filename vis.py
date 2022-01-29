from clustergrammer_widget import *
net = Network(clustergrammer_widget)
net.load_file('C:/Users/Elinor/Desktop/ויזואליזציה של מידע/rc_two_cats.txt')
net.cluster()

# view the results as a widget
net.widget()