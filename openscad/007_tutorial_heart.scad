/*
h1 = 23;
h2 = 10;
h3 = 8;
d1 = 25;
d2 = 12;
d3 = 15;

p0 = [0,0];
p1 = [0,h1+h2];
p2 = [d3,h1];
p3 = [d1+d2,h1+h2];
p4 = [d1+d2,h3];
p5 = [d1,0];

points = [p0,p1,p2,p3,p4,p5];

linear_extrude(height=80)
    polygon(points);
rotate_extrude(angle=360)
    translate([50,0,0])
        polygon(points);

*/

n=500;
h=10;
step=360/n;
points=[for(t=[0:step:359.999]) [16*pow(sin(t),3), 13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t)] ];
linear_extrude(height=h)
    polygon(points);
