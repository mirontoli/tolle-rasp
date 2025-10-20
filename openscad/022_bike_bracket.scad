// L-shaped bicycle bracket with holes

// Dimensions
length = 40;  
width = 30;       
height = 8;      
bolt_hole_diameter = 6;
slot_width = 7;
slot_length = 20;
bolt_hole_radius = bolt_hole_diameter/2;
//Vertical flat bracket
vertical_bracket_height = height/2;


// bottom bracket
module bottom_bracket() {
    translate([0, 0, 0])
    cube([length, width, height]);
}

module hole() {
    union() {
        cylinder(h=height+2, r=bolt_hole_radius, $fn=32);
        //inbuktning for nuts
        cylinder(h=3, r=bolt_hole_radius+3, $fn=32);
    }
}

// Subtract bolt holes from bottom piece
module bottom_holes() {
    // First bolt hole (centered along length, closer to one side)
    translate([12, width/2, -1])
        hole();
    
    // Second bolt hole (centered along length, toward other side)
    translate([27, width/2, -1])
        hole();
}

module bottom_bracket_w_holes() {
    difference() {
        bottom_bracket();
        bottom_holes();
    }
}



module bracket() {
    cube([length, width, vertical_bracket_height]);
}

// Elongated slot (centered on the bracket)
module slot() {
    translate([length/2 - slot_length/2, width/2 - slot_width/2, -1])
        cube([slot_length, slot_width, vertical_bracket_height + 2]);
}
//slot();
// Final bracket with slot
module vertical_bracket() {
    rotate([0,-90,0])
        translate([0, 0, -vertical_bracket_height])
            difference() {
                bracket();
                slot();
            }
}

//vertical_bracket();
//bottom_bracket_w_holes();

// Final L bracket
module final_l_bracket() {
   union() {
       vertical_bracket();
       bottom_bracket_w_holes();
   }
}

minkowski() {
    final_l_bracket();
    sphere(r=1, $fn=2);
}
