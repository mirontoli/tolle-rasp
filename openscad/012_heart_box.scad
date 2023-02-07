$fa=1;
$fs=0.5;

function heart_coordinates(t) = [16*pow(sin(t),3), 13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t)];

//function heart_coords2(t) = [(pow(

module heart(h=10) {   
    n=500;
    step=360/n;
    points=[for(t=[0:step:359.999]) heart_coordinates(t) ];
    linear_extrude(height=h)
        polygon(points);
}
module heart_emoji(h=10) {
    linear_extrude(h)
        text("\u2665",size=30);
}

module heart_box() {
    difference() {
        heart();
        #translate([0,0,2])
            scale([0.8,0.8,1])
                heart();
        translate([0,0,9])
            scale([0.9,0.9,1])
                heart();
        
    }
}

module heart_lid() {
    translate([0,0,3])
        rotate([180,0,180])
            difference() {
                union() {
                    translate([0,0,1])
                        heart(h=2);
                    scale([0.9,0.9,1])
                        heart(h=3);
                }
                translate([-9,-1,2])
                    linear_extrude(4)
                        text("Jenny",size=5);
            }
}

//heart();
//heart_box();

//translate([40,0,0])
//    heart_lid();

//heart_emoji();

// a square and two semi-circles
module heart_simple(r=5, h=10) {
    side = r*2;
    rotate([0,0,45])
        linear_extrude(h) 
            union() {
                square(side, center=false);

                translate([side,r,0])
                    circle(r);

                translate([r,side,0])
                    circle(r);
            }
 }
 
 //heart_simple(r=10);
 
 //overriding heart to reuse the previous modules
 //only default values are supported
 //not useful in this case because this one is not centered
 //screw generics
 //module heart() { heart_simple(); }
 //heart_box();


// function translate_y
//side = side of the square
//height is the hypotenuse of the isosceles triangle
//use pythogorean formula
//side_x_side = side*side;
//height = sqrt(side_x_side + side_x_side);
//scaled_height = height*scaling;
//margins = height - scaled_height;
//translate_y = margins/2;
function translate_y(side,scaling) = (sqrt(2*side*side)-sqrt(2*side*side)*scaling)/2;
 
module heart_box_simple(r=10,h=10) {
    side = r*2;
    scaling_inner = 0.8;
    scaling_outer = 0.9;
    translated_y_inner = translate_y(side, scaling_inner);
    translated_y_outer = translate_y(side, scaling_outer);
    z_outer = h-1;
    echo("y outer", translated_y_outer);
    difference() {
       heart_simple(r=r);
       translate([0,translated_y_inner,2])
           scale([scaling_inner,scaling_inner,1])
               heart_simple(r=r);
       translate([0,translated_y_outer,z_outer])
           scale([scaling_outer,scaling_outer,1])
               heart_simple(r=r);
     }
 }
 module heart_box_lid_simple(r=10,h=3) {
     heart_simple(r=r);
     translate([0,0,1])
        scale([0,0,0.9])
            heart_simple(r=r);
 }
 //heart_box_simple();
 heart_box_lid_simple();
 
 