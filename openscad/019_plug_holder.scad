$fa=1;
$fs=0.4;

// cube electrical plug
side_width = 77;
thickness = 1.6; //wall width 0.8 * 2
holder_width = 8;
top_plate_length = side_width/2;

module side (
    side_width=side_width) {
    cube([side_width, thickness, holder_width]);
}


// right side
translate([0,0,0])
    rotate([0,0,0])
        side();

// left side
translate([0, side_width+thickness, 0])
    rotate([0,0,0])
        side();

// bottom side
//translate([0, side_width+thickness, 0])
    rotate([0,0,90])
        side(side_width = side_width + thickness *2 );



module top_plate() {
    difference() {
        side(side_width = top_plate_length );
        translate([top_plate_length/2,-thickness/2,holder_width/2])        
            rotate([-90,0,0]) 
                cylinder(h=2,r=2.5);
        translate([top_plate_length/2,-1,holder_width/2])        
            rotate([-90,0,0]) 
                cylinder(h=thickness+2,r=1);
    }
}

// right top plate
translate([side_width-thickness, thickness, 0])
    rotate([0,0,-90])
        top_plate();

// left top plate
translate([side_width-thickness, side_width + thickness + top_plate_length, 0])
    rotate([0,0,-90])
        top_plate();