//pipe bowl
//@mirontoli 2023-01-05
//https://www.thingiverse.com/thing:5769091/files
$fa=1;
$fs=0.4;
difference() {
    rotate_extrude(angle=360) {
        translate([8,0])
            square([16,40],center=true);
        translate([16,0])
            resize([10,0])
                circle(r=20);    
    }
    translate([0,0,20])
        resize([25,25,35])
        sphere(r=20);
    translate([0,0,-10])
        rotate([0,90,0])
            cylinder(h=25,r=4.05);
}
