    // Master Yoda 3D Model
// OpenSCAD file for 3D printing

$fn = 200; // Smooth curves

module yoda() {
    union() {
        // Base/robes
        translate([0, 0, -5])
            cylinder(h = 15, r1 = 12, r2 = 8);
        
        // Torso
        translate([0, 0, 10])
            scale([1, 0.8, 1.2])
                sphere(r = 8);
        
        // Head
        translate([0, 0, 22])
            scale([0.9, 0.85, 1])
                sphere(r = 6);
        
        // Large ears
        translate([-7, -1, 24])
            rotate([0, -15, -20])
                scale([2.5, 1, 0.3])
                    sphere(r = 3);
        
        translate([7, -1, 24])
            rotate([0, 15, 20])
                scale([2.5, 1, 0.3])
                    sphere(r = 3);
        
        // Ear tips (pointed)
        translate([-11, -1, 26])
            rotate([0, -15, -20])
                scale([1.2, 0.8, 0.2])
                    sphere(r = 1.5);
        
        translate([11, -1, 26])
            rotate([0, 15, 20])
                scale([1.2, 0.8, 0.2])
                    sphere(r = 1.5);
        
        // Forehead wrinkles
        translate([0, 4, 25])
            rotate([90, 0, 0])
                cylinder(h = 1, r = 3);
        
        translate([0, 4, 26.5])
            rotate([90, 0, 0])
                cylinder(h = 1, r = 2.5);
        
        // Arms
        translate([-6, 0, 15])
            rotate([0, -10, -30])
                cylinder(h = 8, r = 1.5);
        
        translate([6, 0, 15])
            rotate([0, 10, 30])
                cylinder(h = 8, r = 1.5);
        
        // Hands
        translate([-8, -3, 20])
            sphere(r = 1.8);
        
        translate([8, -3, 20])
            sphere(r = 1.8);
        
        // Walking stick/lightsaber (optional)
        translate([12, -3, 10])
            cylinder(h = 25, r = 0.3);
        
        translate([12, -3, 35])
            sphere(r = 0.5);
    }
    
    // Subtract eye sockets
    difference() {
        union() {} // Empty union for difference operation
        
        translate([-1.5, 4.5, 24])
            sphere(r = 0.8);
        
        translate([1.5, 4.5, 24])
            sphere(r = 0.8);
        
        // Mouth area
        translate([0, 4.2, 21])
            rotate([90, 0, 0])
                scale([1.5, 0.8, 1])
                    cylinder(h = 1, r = 0.5);
    }
}

// Add eyes as separate objects
module yoda_eyes() {
    // Eye spheres
    translate([-1.5, 4.2, 24])
        sphere(r = 0.6);
    
    translate([1.5, 4.2, 24])
        sphere(r = 0.6);
}

// Create the complete model
difference() {
    yoda();
    
    // Eye sockets
    translate([-1.5, 4.5, 24])
        sphere(r = 0.8);
    
    translate([1.5, 4.5, 24])
        sphere(r = 0.8);
    
    // Mouth
    translate([0, 4.2, 21])
        rotate([90, 0, 0])
            scale([1.5, 0.8, 1])
                cylinder(h = 1, r = 0.5);
}

// Add eyes
yoda_eyes();

// Optional: Add a simple base for stability
translate([0, 0, -12])
    cylinder(h = 2, r = 15);