

module heart(h=10) {   
    n=500;
    step=360/n;
    points=[for(t=[0:step:359.999]) [16*pow(sin(t),3), 13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t)] ];
    linear_extrude(height=h)
        polygon(points);
}
module heart_box() {
    difference() {
        heart();
        translate([0,0,2])
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

heart_box();

translate([40,0,0])
    heart_lid();

