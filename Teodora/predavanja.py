import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import matplotlib.lines as lns
plt.rcParams['figure.figsize']=(15, 10)

def plot_function(interval,fun):
    a=interval[0]
    b=interval[1]

    x=np.linspace(a,b,100)
    y1=fun(x)
    plt.plot(x,y1, linewidth=5)

def plot_tangent(point,k):
    limits=plt.axis()
    x=np.linspace(limits[0],limits[1],100)
    plt.plot(x,point[1]+k*(x-point[0]), linewidth=5)

def plot_dotted_lines(x,y,label_x,label_y,limits):
    plt.autoscale(False)
    plt.hlines(y=y, xmin=limits[0], xmax=x,linestyle="--",color="magenta")
    plt.vlines(x=x, ymin=limits[2], ymax=y,linestyle="--",color="magenta")
    plt.text(limits[0],y,label_y,fontsize = 20)
    plt.text(x,limits[2],label_x,fontsize = 20)

def plot_markers(marker_list,labels_x,labels_y,limits):
    for i in range(len(marker_list[0])):
        plt.plot(marker_list[0][i],marker_list[1][i],'o',markersize=15,markerfacecolor='r')
        plot_dotted_lines(marker_list[0][i],marker_list[1][i],labels_x[i],labels_y[i],limits)

def plot_tangents(tangent_list,ode):
 if len(tangent_list) > 0:
    for i in range(len(tangent_list[0])):
        x = tangent_list[0][i]
        y = tangent_list[1][i]
        plot_tangent([x,y],ode(x,y))
 return plt.axis()

def plot_euler_step(x0,y0,step,ode):
    [x0,x1,y0,y1]=get_values_euler(x0,y0,step,ode)

    plot_function([x0-0.05,x1+0.05],fun)

    tangent_list=[[x0],[y0]]
    limits=plot_tangents(tangent_list,ode)

    marker_list=[[x0,x1],[y0,y1]]
    labels_x =['X_0','X_0+h']
    labels_y =['Y_0','y_1']
    plot_markers(marker_list,labels_x,labels_y,limits)

def get_values_euler(x0,y0,step,ode):
    x1 = x0 + step
    y1 = y0 + step*ode(x0, y0)
    return [x0,x1,y0,y1]

def plot_mp_step(x0,y0,step,ode,method_st):
    [x0,x1_2,x1,y0,y1_2,y1] = get_values_mp(x0,y0,step,ode)

    plot_function([x0-0.05,x1+0.05],fun)

    tangent_list=[[x0],[y0]]
    marker_list=[[x0,x1_2],[y0,y1_2]]
    labels_x =['X_0','X_0+1/2*h']
    labels_y =['Y_0','y_1/2']

    if method_st == 2:
        tangent_list=[[x1_2],[y1_2]]
        marker_list=[[x0,x1_2],[y0,y1_2]]
        labels_x =['X_0','X_0+1/2*h']
        labels_y =['Y_0','y_1/2']
    elif method_st == 3:
        tangent_list=[[x1_2],[y1_2]]
        marker_list=[[x0,x1_2,x1],[y0,y1_2,y1]]
        labels_x =['X_0','X_0+h/2','X_1=X_0+h']
        labels_y =['Y_0','y1/2','Y_1']
        ln=lns.Line2D(xdata=[x0,x1],ydata=[y0,y1],linewidth=5,color='black')
        ax = plt.gca()
        ax.add_line(ln)
    limits=plot_tangents(tangent_list,ode)
    plot_markers(marker_list,labels_x,labels_y,limits)


def get_values_mp(x0,y0,step,ode):
    x1_2 = x0 + step/2
    x1 = x0 + step
    y1_2 = y0 + step/2 * ode(x0, y0)
    y1 = y0 + step * ode(x1_2, y1_2)
    return [x0,x1_2,x1,y0,y1_2,y1]

def plot_heun_step(x0,y0,step,ode,method_st):
    [x0,x1,y0,y1_0,y1] = get_values_heun(x0,y0,step,ode)

    plot_function([x0-0.05,x1+0.05],fun)

    tangent_list=[[x0],[y0]]
    marker_list=[[x0,x1],[y0,y1_0]]
    labels_x =['X_0','X_0+h']
    labels_y =['Y_0','y_1_0']

    if method_st == 2:
        tangent_list=[[x0,x1],[y0,y1_0]]
        marker_list=[[x0,x1],[y0,y1_0]]
        labels_x =['X_0','X_0+h']
        labels_y =['Y_0','y_1_0']
    elif method_st == 3:
        tangent_list=[[x0,x1],[y0,y1_0]]
        marker_list=[[x0,x1,x1],[y0,y1_0,y1]]
        labels_x =['X_0','X_1=X_0+h','X_1=X_0+h']
        labels_y =['Y_0','y_{0,1}','Y_1']
        ln=lns.Line2D(xdata=[x0,x1],ydata=[y0,y1],linewidth=5,color='black')
        ax = plt.gca()
        ax.add_line(ln)
    limits=plot_tangents(tangent_list,ode)
    plot_markers(marker_list,labels_x,labels_y,limits)

def get_values_heun(x0,y0,step,ode):
    x1 = x0 + step
    y1_0 = y0 + step*ode(x0, y0)

    y1 = y0 + step/2*(ode(x0, y0)+ode(x1, y1_0))
    return [x0,x1,y0,y1_0,y1]

def get_values_rk4(x0, y0, step, ode):
    x1_2 = x0 + step/2
    x1 = x0 + step

    k1 = step*ode(x0, y0)
    y1_2_1 = y0 + 1/2*k1

    k2 = step*ode(x1_2, y1_2_1)
    y1_2_2 = y0 + 1/2*k2

    k3 = step*ode(x1_2, y1_2_2)
    y1_1 = y0 + k3

    k4 = step*ode(x1, y1_1)
    y1 = y0 + 1/6*(k1+2*k2+2*k3+k4)

    return [x1, x1_2 , y1_2_1, y1_2_2, y1_1, y1]

def plot_rk4_step(x0,y0,step,ode,method_st):
    [x1, x1_2 , y1_2_1, y1_2_2, y1_1, y1] = get_values_rk4(x0,y0,step,ode)

    plot_function([x0-0.05,x1+0.05],fun)

    tangent_list=[[x0],[y0]]
    marker_list=[[x0,x1_2],[y0,y1_2_1]]
    labels_x =['X_0','X_0+1/2*h']
    labels_y =['Y_0','y_1/2']

    if method_st == 2:
        tangent_list=[[x1_2],[y1_2_1]]
    elif method_st == 3:
        tangent_list=[]
        marker_list=[[x0,x1_2],[y0,y1_2_2]]
        labels_x =['X_0','X_1=X_0+1/2h']
        labels_y =['Y_0','y_1/2_1']
        ln=lns.Line2D(xdata=[x0,x1_2],ydata=[y0,y1_2_2],linewidth=5,color='black')
        ax = plt.gca()
        ax.add_line(ln)
    elif method_st == 4:
        tangent_list=[[x1_2],[y1_2_2]]
        marker_list=[[x0,x1_2],[y0,y1_2_2]]
        labels_x =['X_0','X_1=X_0+1/2h']
        labels_y =['Y_0','y_1/2_1']
    elif method_st == 5:
        tangent_list=[]
        marker_list=[[x0,x1],[y0,y1_1]]
        labels_x =['X_0','X_1=X_0+h']
        labels_y =['Y_0','y1_1']
        ln=lns.Line2D(xdata=[x0,x1],ydata=[y0,y1_1],linewidth=5,color='black')
        ax = plt.gca()
        ax.add_line(ln)
    elif method_st == 6:
        tangent_list=[[x1],[y1_1]]
        marker_list=[[x0,x1],[y0,y1_1]]
        labels_x =['X_0','X_1=X_0+h']
        labels_y =['Y_0','y1_1']
    elif method_st == 7:
        tangent_list=[]
        marker_list=[[x0,x1],[y0,y1_1]]
        labels_x =['X_0','X_1=X_0+h']
        labels_y =['Y_0','y1']
        ln=lns.Line2D(xdata=[x0,x1],ydata=[y0,y1],linewidth=5,color='black')
        ax = plt.gca()
        ax.add_line(ln)

    limits=plot_tangents(tangent_list,ode)
    plot_markers(marker_list,labels_x,labels_y,limits)

def plot_rk4_all(x0,y0,step,ode):
    [x1, x1_2 , y1_2_1, y1_2_2, y1_1, y1] = get_values_rk4(x0,y0,step,ode)

    plot_function([x0,x1],fun)

    tangent_list=[[x0,x1_2,x1_2,x1],[y0,y1_2_1,y1_2_2,y1_1]]
    marker_list=[[x0,x1_2,x1_2,x1,x1],[y0,y1_2_1,y1_2_2,y1_1,y1_1]]
    labels_x =['X_0','X_0+1/2*h','X_0+1/2*h','X_1=X_0+h','X_1=X_0+h']
    labels_y =['Y_0','y_1/2','y_1/2_1','y1_1','y1']

    limits=plot_tangents(tangent_list,ode)
    plot_markers(marker_list,labels_x,labels_y,limits)

    plt.gca().get_lines()[1].set_color("red")
    plt.gca().get_lines()[2].set_color("green")
    plt.gca().get_lines()[3].set_color("yellow")
    plt.gca().get_lines()[4].set_color("black")

    plt.plot([], [], ' ', label="Crvena - K1 - tangenta u (X0,y0)")
    plt.plot([], [], ' ', label="Zelena - K2 - tangenta u (X_0+1/2*h,y_1/2)")
    plt.plot([], [], ' ', label="Zuta - K3 - tangenta u (X_0+1/2*h,y_1/2_1)")
    plt.plot([], [], ' ', label="Crna - K4 - tangenta u (X_0+h,y1_1)")
    plt.legend(prop={"size":16})

def calculate_error(x0,xn,y0,ode,fun,min_st_size,method):
    step = 1
    errors=[]
    sub_intervals=[]
    while(step >= min_st_size):
        x = np.arange(x0,xn+step,step)
        y = method(x0,xn,y0,step,ode)
        errors.append(np.mean(np.abs(fun(x)-y)))
        sub_intervals.append(step)
        step = step / 2

    plt.plot(np.arange(0,len(errors)),errors, linewidth = 5)
    plt.xlabel('Indeks i greska, za koju vazi: h=1/2**{i-1}. Npr. za i=1 je h=1, za i=2 je h=1/2 itd.', fontsize=18)
    plt.ylabel('Greska', fontsize=18)
    return [errors,sub_intervals]

def linterp(x,y):
    n = len(x)
    p = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L = np.convolve(np.array([1, -x[j]])/(x[i]-x[j]), L)
        p = p + y[i]*L

    return p


def ojler(x0,xn,y0,h,odj):
    x = np.arange(x0,xn+h,h)
    n = len(x)
    y = np.zeros(n)
    y[0] = y0
    for i in range(1,n):
        y[i] = y[i-1] + h * odj(x[i-1], y[i-1])
    return y
