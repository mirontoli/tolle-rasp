/*
    Box without top
    Inside: length 28 mm, width 20 mm, height 10 mm
    Wall thickness: 2 mm
*/

inner_length = 28;
inner_width  = 20;
inner_height = 10;
inner = [inner_length, inner_width, inner_height];
wall = 2;
pcb_thickness = 2;


outer = [inner_length + 2*wall, inner_width + 2*wall, inner_height + wall - 1];
// USB-C opening on one short side
usb_width = 7; // opening width in mm
usb_y = outer[1]/2 - usb_width/2; // centered along the short axis
cutout = [wall+2, usb_width, inner_height+1];

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

difference() {
    // outer shell
    //cube(outer, center = false);
    //rounded_box(outer, r = corner_radius);
    hull_box(outer, r = corner_radius);
    // inner cavity (translated up by wall thickness to create bottom)
    translate([wall, wall, wall])
        //cube(inner, center = false);
        hull_box(inner, r = corner_radius);
    // cut a rectangular opening on one short side (front at y=0)
    // depth: reach through outer wall into inner cavity but not across entire width
    translate([-1, usb_y, wall + pcb_thickness])   
        cube(cutout, center = false);
    // cut out a rectangular opening on the opposite short side for output cables
    translate([outer[0]- wall- 1, usb_y, wall + pcb_thickness])
        cube(cutout, center = false);
}