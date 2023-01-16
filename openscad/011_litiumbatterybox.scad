use <MCAD/boxes.scad>
$fa=1;
$fs=0.8;

wall_thickness = 2; 

inner_length = 98; // x
inner_width = 66; // y
inner_height=3.5; // z
lid_step = 1;
divider = 1;
regulator_length = 15;
regulator_width = 20;
regulator_height = 10;
cable_opening = 5;


box_radius = 1;

outer_length = wall_thickness + inner_length + wall_thickness;
outer_width = wall_thickness + inner_width + wall_thickness;
outer_height = wall_thickness + inner_height + lid_step;  

inner_ext_length = inner_length + divider + regulator_length;
outer_ext_length = wall_thickness + inner_ext_length + wall_thickness;

outer_ext_height = wall_thickness + regulator_height + lid_step;

divider_width = inner_width - cable_opening - regulator_width;

module main_box() {
    difference() {
           
        translate([outer_ext_length/2,outer_width/2,outer_height/2])
            roundedBox(size=[outer_ext_length,outer_width,outer_height],radius=box_radius,sidesonly=true);

        //inner box
        translate([wall_thickness,wall_thickness,wall_thickness])
            cube([inner_ext_length,inner_width,outer_height]);
        //lid step
        translate([wall_thickness-1, wall_thickness-1, outer_height-1])
            cube([inner_ext_length+lid_step*2,inner_width+lid_step*2,lid_step+1]);

    }
    
}

main_box();
//divider
translate([wall_thickness+inner_length, wall_thickness + regulator_width, wall_thickness-0.01])
    cube([divider,divider_width,inner_height]);

