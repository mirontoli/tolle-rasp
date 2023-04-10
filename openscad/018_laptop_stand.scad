// downloaded round-anything lib from https://github.com/Irev-Dev/Round-Anything
// simplifying 3d print, page 212

use <Round-Anything/roundAnythingExamples.scad>;
$fn=200;
thickness=5;
linear_extrude(thickness)   
    shell2d(0,-12) {
        import("018_frame.svg",center=true);
    }
