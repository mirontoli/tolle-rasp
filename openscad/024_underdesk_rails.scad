/*
This is for having apple tv mounted under desk 
but it can be use for any other devices
the size is customizable, 
print two pieces of the same rail and mount them on the desk
because the design is symmetric, 
the distance between screws is fixed so that you can resize the length as you want
*/

wall = 3; // wall thickness
inner_height = 33; // height of internal cavity
length = 100; // length of the rail
inner_width = 20; // width of the rail
outer_width = inner_width + wall;
hole_y = inner_width / 2 + wall;
hole_distance = 50; // make sure it it is not bigger than length
hole_x1 = (length - hole_distance) / 2;
hole_x2 = hole_x1 + hole_distance;
screw_hole_radius = 1.5;
screw_driver_radius = 4;
screw_sink_depth = 1;
screw_sink_radius = 3; // radius of the countersink for the screw head

cube_outer = [length, outer_width, inner_height + 2*wall];
cube_inner = [length+2, inner_width+2, inner_height];

// lay down for easier printing
rotate([90,0,0])
    difference() {
        // outer shell
        cube(cube_outer, center = false);
        // inner cavity (translated up by wall thickness to create bottom)
        translate([-1, wall, wall])
            cube(cube_inner, center = false);
        // screw holes
        translate([hole_x1, hole_y, -1])
            cylinder(h=inner_height + 2*wall+2, r=screw_hole_radius, center=false);
        translate([hole_x2, hole_y, -1])
            cylinder(h=inner_height + 2*wall+2, r=screw_hole_radius, center=false);
        // screw driver clearance
        translate([hole_x1, hole_y, -1])
            cylinder(h=wall+2, r=screw_driver_radius, center=false);
        translate([hole_x2, hole_y, -1])
            cylinder(h=wall+2, r=screw_driver_radius, center=false);
        // screw head countersink
        translate([hole_x1, hole_y, wall + inner_height - screw_sink_depth])
            cylinder(h=wall, r=screw_sink_radius, center=false);
        translate([hole_x2, hole_y, wall + inner_height - screw_sink_depth])
            cylinder(h=wall, r=screw_sink_radius, center    =false);    
    }