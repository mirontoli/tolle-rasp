//Car 
//Tutorial: https://en.wikibooks.org/wiki/OpenSCAD_Tutorial/Chapter_1

$fa=1;
$fs=0.4;
//main part of the car
cube([60,20,10],center=true);
//upper part of the car
translate([0,0,10-0.001])
    cube([30,20,10],center=true);
//wheel 1
translate([-20,-15,0])
    rotate([90,0,0])
    cylinder(h=3,r=8,center=true);
//wheel 2
translate([-20,15,0])
    rotate([90,0,0])
    cylinder(h=3,r=8,center=true);
//wheel 3
translate([20,15,0])
    rotate([90,0,0])
    cylinder(h=3,r=8,center=true);
//wheel 4
translate([20,-15,0])
    rotate([90,0,0])
    cylinder(h=3,r=8,center=true);
//axle 1
translate([20,0,0])
    rotate([90,0,0])
    cylinder(h=30,r=2, center=true);
//axle 2
translate([20,0,0])
    rotate([90,0,0])
    cylinder(h=3,r=2, center=true);

//axle 3
translate([-20,0,0])
    rotate([90,0,0])
    cylinder(h=30,r=2, center=true);
//axle 4
translate([-20,0,0])
    rotate([90,0,0])
    cylinder(h=3,r=2, center=true);