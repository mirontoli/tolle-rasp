/*
    Box enclosure for EKM-024 USB-C lock module
    Inside: length 28 mm, width 20 mm, height 10 mm
    Wall thickness: 2 mm
    @mirontoli 2026-01-02
*/

inner_length = 28;
inner_width  = 20;
inner_height = 8;
inner = [inner_length, inner_width, inner_height];
wall = 2;
pcb_thickness = 2;


outer = [inner_length + 2*wall, inner_width + 2*wall, inner_height + wall -1];
// USB-C opening on one short side
usb_width = 9; // opening width in mm
usb_y = outer[1]/2 - usb_width/2; // centered along the short axis
cutout_usb = [wall+2, usb_width, inner_height+1];

screw_header_width = 6;
screw_header_y = outer[1]/2 - screw_header_width/2;
cutout_screw = [wall+2, screw_header_width, inner_height+1];

corner_radius = 0.5; // adjust; must be < min(outer)/2

module rounded_box(size, r=1.5, fn=24) {
    // size = [x,y,z]. final bbox == size
    minkowski() {
        cube([size[0]-2*r, size[1]-2*r, size[2]-2*r], center = false);
        sphere(r = r, $fn = fn);
    }
}

// ...existing code...
// replace the outer cube() with a hull-based outer to get rounded corners
module hull_box(size, r=0.5, fn=24) {
    hull() {
        for (x=[0, size[0]])
            for (y=[0, size[1]])
                for (z=[0, size[2]])
                    translate([x,y,z]) sphere(r=r, $fn=fn);
    }
}

// the rail to connect the lock
module rail(length = outer[0]+2) {
    rotate([45,0,0])
        cube([length, 1, 1], center = false);
}

difference() {
    // outer shell
    cube(outer, center = false);
    //rounded_box(outer, r = corner_radius);
    //hull_box(outer, r = corner_radius);
    // inner cavity (translated up by wall thickness to create bottom)
    translate([wall, wall, wall])
        cube(inner, center = false);
        //hull_box(inner, r = corner_radius);
    // cut a rectangular opening on one short side (front at y=0)
    // depth: reach through outer wall into inner cavity but not across entire width
    translate([-1, usb_y, wall + pcb_thickness])   
        cube(cutout_usb, center = false);
    // cut out a rectangular opening on the opposite short side for output cables
    translate([outer[0]- wall- 1, screw_header_y, wall + pcb_thickness])
        cube(cutout_screw, center = false);
    // cut out the rail slot on top
    translate([-1, 0, outer[2]-2])
        rail();
    // cut out the rail slot on top
    translate([-1, outer[1]+0, outer[2]-2])
        rail();
}
// Lid
lid_outer_height = wall + 3;
lid_outer = [outer[0], outer[1]+2*wall, lid_outer_height];
lid_inner = [inner_length + 2*wall + 2, outer[1], lid_outer_height];
label = "5V 3A";
label_size = 5;
label_len = len(label);
echo("Label length: ", label_len);
label_x = 7; //lid_outer[0]/2 - label_len/2;
label_y = lid_outer[1]/2 - label_size/2;

!union() {
    difference() {
        // outer lid
        cube(lid_outer, center = false);
        // inner cavity of lid
        translate([-1, wall, -wall])
            cube(lid_inner, center = false);
        translate([label_x, label_y, lid_outer_height - 0.8])
            linear_extrude(height=1)
                text(label, size=label_size, halign="left", valign="baseline"); 
    }
    // rails on lid
    translate([0, wall, 0])
        rail(length = lid_outer[0]);
    translate([0, lid_outer[1] - wall, 0])
        rail(length = lid_outer[0]);
}



difference() {
    cube(lid_outer, center = false);
    translate([label_x, label_y, lid_outer_height - 0.8])
        linear_extrude(height=1)
            text(label, size=label_size, halign="left", valign="baseline");
}







