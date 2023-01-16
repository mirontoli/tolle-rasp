//Car 
//Tutorial: https://en.wikibooks.org/wiki/OpenSCAD_Tutorial/Chapter_4
module wheel(wheel_radius=8, side_spheres_r=50, hub_thickness=4,cyl_r=2) {
    what=side_spheres_r+hub_thickness/2;
    cyl_h=2*wheel_radius;
    difference() {
        //wheel sphere
        sphere(r=wheel_radius);
        //side sphere 1
        translate([0,what,0])
            sphere(r=side_spheres_r);
        //side sphere 2
        translate([0,-what,0])
            sphere(r=side_spheres_r);
        //cylinder 1
        translate([wheel_radius/2,0,0])
            rotate([90,0,0])
                cylinder(h=cyl_h,r=cyl_r,center=true);
        //cylinder 2
        translate([0,0,wheel_radius/2])
            rotate([90,0,0])
                cylinder(h=cyl_h,r=cyl_r,center=true);
        //cylinder 3
        translate([-wheel_radius/2,0,0])
            rotate([90,0,0])
                cylinder(h=cyl_h,r=cyl_r,center=true);
        //cylinder 4
        translate([0,0,-wheel_radius/2])
            rotate([90,0,0])
                cylinder(h=cyl_h, r=cyl_r,center=true);
    } 
}
module body(base_height=10,top_height=10) {
    body_transl_z = base_height/2+top_height/2-0.001;
    resize([90,20,12])
        sphere(r=base_height);
    //upper part of the car
    translate([5,0,body_transl_z])
        resize([50,15,15])
            sphere(r=top_height);
}

module axle(track=40,radius=2) {
    rotate([90,0,0])
        cylinder(h=track,r=radius, center=true);
}
//$fa=1;
//$fs=0.4;

wheel_turn = 20;
body_roll = -5;
track = 35;
wheelbase = 40;


//main part of the car
rotate([body_roll,0,0]) {
    body();
}
//wheel front left
translate([-20,-track/2,0])
    rotate([0,0,wheel_turn])
        wheel();
//wheel front right
translate([-20,track/2,0])
    rotate([0,0,wheel_turn])
        wheel();
//wheel rear left
translate([20,-track/2,0])
    rotate([0,0,0])
        wheel(wheel_radius=10);
//wheel rear right
translate([20,track/2,0])
    rotate([0,0,0])
        wheel(wheel_radius=10);
//axle 1
translate([wheelbase/2,0,0])
    axle();
//axle 2
translate([-wheelbase/2,0,0])
    axle();