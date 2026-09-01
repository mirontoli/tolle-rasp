
/*
mounting bracket for tv set cables
@mirontoli 
version 5 2026-09-01
*/
w=160;
d=50;
h=5;
eps = 0.01;
screw_hole_r = 2;
screw_hole_x_pad = 30;
screw_hole_x_pad_opposite = w - screw_hole_x_pad;
screw_hole_d = 23;
screw_mount_r = 5;
screw_mount_d = screw_hole_d + screw_hole_r*2.4;
gusset_w = 18;
w_cable = 50;
d_cable = 25;

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
                cylinder(h=h+2*eps, r=screw_hole_r);
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

module cable_hole() {
    translate([w/2-w_cable/2,-eps,-eps]) 
        difference() {
            cube([w_cable,d_cable+eps,d_cable+eps]);
            rotate([0, -45, 0])
                cube([w_cable, d_cable+2*eps, d_cable+2*eps]);
            rotate([0, 45, 0])
                translate([0, -eps, 36])
                    cube([w_cable, d_cable+3*eps, d_cable+2*eps]);
        }
}

module mounting_bracket() {
    difference() {
        union() {
            vertical_plate();
            horizontal_plate();
            full_width_gusset();
        }
        cable_hole();
    }
}

mounting_bracket();

// test print
!difference() {
    mounting_bracket();
    translate([w/4, -eps, -eps])
        cube([2*w,2*d,2*d]);
}

