
// Simplifying 3D printing book
// chapter 6, page 143
// BOSL downloaded from https://github.com/revarbat/BOSL
// saved in ~\Documents\OpenSCAD\libraries
use <BOSL/shapes.scad>;
$fn = 200;
width = 180;
length = 67;
height = 40;
rail_size = 10;
hollow_factor_width = 0.95;
hollow_factor_length = 0.85;
hollow_factor_height = 0.90;
module create_tray() {
    difference() {
        cuboid([width,length,height], fillet=10);
        scale([hollow_factor_width,hollow_factor_length, hollow_factor_height])
            cuboid([width,length,height],fillet=10);
        translate([0,0,height])
            cube([width*2,length*2,height*2], center=true);
    }
}

use <BOSL/sliders.scad>;
module create_rail() {
    translate([width/2, 0, -(rail_size/2)])
        rotate([0,90,0])
            rail(l=length-20, w=rail_size, h=rail_size);
}
module create_handle(size) {
    translate([0,-length/2, -(size*1.5)])
        difference() {
            difference() {
                cuboid([5*size, 3*size, 1.5*size], fillet=2);
                scale([0.8,0.8,2])
                    cuboid([5*size, 3*size, 1.5*size], fillet=2);
            }
            translate([0,size*50,0])
                cube([size*100, size*100,size*100], center=true);    
        }
}
module create_3mm_screw_hole() {
    union() {
        cylinder(d=3, h=500);
        translate([0,0,-500])
            cylinder(d=10,h=500);
    }
}
module create_slider(offset) {
    base = 20;
    hole_inset=20;
    difference() {
        translate([width/2+(rail_size+base),0,-rail_size/2])
            rotate([0,-90,0])
                slider(l=length, h=rail_size,base=base, wall=4, slop=offset);
        translate([width/2+(rail_size+(base/2)),(length/2)-hole_inset, -rail_size/2])
            create_3mm_screw_hole();
        translate([width/2+(rail_size+(base/2)),-((length/2)-hole_inset), -rail_size/2])
            create_3mm_screw_hole();
    }
}

// 5% infill, support, build plate adhesion none.
create_tray();
create_rail();
mirror([1,0,0]) create_rail();
// create_handle(10);

// slider x2, 5% infill, no support, rotate in slicer, approx 1 hr to print
// create_slider(0.4);

// mirror([1,0,0]) create_slider(0.4);
