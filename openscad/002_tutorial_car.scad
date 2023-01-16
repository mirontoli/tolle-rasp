//Car 
//Tutorial: https://en.wikibooks.org/wiki/OpenSCAD_Tutorial/Chapter_2

$fa=1;
$fs=0.4;
wheel_radius = 8;
wheel_width = 3;
wheel_turn = 20;
body_roll = -5;
track = 30;
base_height = 10;
top_height = 10;
body_transl_z = base_height/2+top_height/2-0.001;
//main part of the car
//scale([1.2,1,1]) {
rotate([body_roll,0,0]) {
    cube([60,20,base_height],center=true);
    //upper part of the car
    translate([5,0,body_transl_z])
        cube([30,20,top_height],center=true);
}
//wheel front left
translate([-20,-track/2,0])
    rotate([90,0,wheel_turn])
    cylinder(h=wheel_width,r=wheel_radius,center=true);
//wheel front right
translate([-20,track/2,0])
    rotate([90,0,wheel_turn])
    cylinder(h=wheel_width,r=wheel_radius,center=true);
//wheel rear left
translate([20,-track/2,0])
    rotate([90,0,0])
    cylinder(h=wheel_width,r=wheel_radius,center=true);
//wheel rear right
translate([20,track/2,0])
    rotate([90,0,0])
    cylinder(h=wheel_width,r=wheel_radius,center=true);
//axle 1
translate([20,0,0])
    rotate([90,0,0])
    cylinder(h=track,r=2, center=true);
//axle 2
translate([-20,0,0])
    rotate([90,0,0])
    cylinder(h=track,r=2, center=true);

