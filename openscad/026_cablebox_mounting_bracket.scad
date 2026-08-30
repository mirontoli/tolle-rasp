
/*
mounting bracket for tv set cables
@mirontoli
v1 2026-08-30
*/

w=160;
d=50;
h=3;
eps = 0.01;
screw_hole_r = 2;
screw_hole_x_pad = 30;
screw_hole_x_pad_opposite = w - screw_hole_x_pad;
screw_hole_d = 20;
screw_mount_r = 4;
screw_mount_d = screw_hole_d + screw_hole_r*1.6;
gusset_w = 15;

assert(gusset_w < screw_hole_d - screw_hole_r, 
"the screw hole position must be higher than the gusset");
assert(d > screw_hole_d + screw_hole_r + eps, 
"the depth must be higher than the position depth of the screw hole");
assert(screw_hole_x_pad < w/2 - screw_hole_r - eps, 
"screw hole padding should not be bigger than the half of the widht of mounting bracket");


module vertical_plate() {
    difference() {
        cube([w,d,h]);
        
        translate([screw_hole_x_pad, screw_hole_d, -eps])
            cylinder(h=h+2*eps, r=screw_hole_r);
        translate([screw_hole_x_pad, screw_mount_d, -eps])
            cylinder(h=h+2*eps, r=screw_mount_r);
        
        translate([screw_hole_x_pad_opposite, screw_hole_d, -eps])
            cylinder(h=h+2*eps, r=screw_hole_r);
        translate([screw_hole_x_pad_opposite, screw_mount_d, -eps])
            cylinder(h=h+2*eps, r=screw_mount_r);
    }
}

module horizontal_plate() {
translate([0,h,0]) 
    rotate([90,0,0])
        difference() {       
            cube([w,d,h]);
            translate([screw_hole_x_pad, screw_hole_d, -eps])
                cylinder(h=1.2+2*eps, r=screw_hole_r);
        }
}

module full_width_gusset() {        
    translate([w,0,0])
            rotate([0,270,0])
                linear_extrude(height = w)
                    polygon([
                        [0, 0],
                        [gusset_w, 0],
                        [0, gusset_w]
                    ]);
}

module mounting_bracket() {
    union() {
        vertical_plate();
        horizontal_plate();
        full_width_gusset();
    }
}

mounting_bracket();