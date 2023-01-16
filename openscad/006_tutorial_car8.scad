
$fa = 1;
$fs = 0.4;
module simple_rounded_wheel(
wheel_radius = 12,
wheel_width=4,
tyre_diameter = 6) {
    rotate([90,0,0]) {
        rotate_extrude(angle=360) {
            translate([wheel_radius - tyre_diameter/2, 0])
                circle(d=tyre_diameter);
            translate([0,-wheel_width/2])
                square([wheel_radius - tyre_diameter/2, wheel_width]);
        }
        //cylinder(h=wheel_width,r=wheel_radius-tyre_diameter/2,center=true);
        
    }
}

//simple_rounded_wheel();

module robot_rim(wheel_radius=12,wheel_width=4,tyre_diameter=6,axle_diameter=3) {
    rim_radius=wheel_radius-tyre_diameter/2;
    rotate([90,0,0])
        difference() {
            rotate_extrude(angle=360) {
                difference() {
                    translate([0,-wheel_width/2])
                        square([rim_radius,wheel_width]);
                    translate([rim_radius,0])
                        circle(d=tyre_diameter);
                }
            }
            cylinder(h=wheel_width+1,r=axle_diameter/2,center=true);
        }
}
//robot_rim();
linear_extrude(height=50,center=true,twist=120,scale=1.5)
    scale([2,1,1])
        circle(d=10);