// Grid

module circle_(x, y, z) {
    
    translate([(x+1)*2.5+x*30, (y+1)*2.5+y*30, (z+1)*2.5+z*30])
    translate([15, 15, 15])
    sphere(12);
}

module cross_(x, y, z) {
    
    translate([(x+1)*2.5+x*30, (y+1)*2.5+y*30, (z+1)*2.5+z*30])
    translate([15, 15, 15])
    union() {
        rotate([-45, -45, 0])
        cylinder(h=24, d=4, center=true);
        rotate([45, 45, 0])
        cylinder(h=24, d=4, center=true);
        rotate([-45, -45, 90])
        cylinder(h=24, d=4, center=true);
        rotate([45, 45, 90])
        cylinder(h=24, d=4, center=true);
    }
}

// Main

difference() {
    
    cube(100);
    
    for (x=[0, 1, 2]) {
            
        for (z=[0, 1, 2]) {
                
            translate([(x+1)*2.5+x*30, 0, (z+1)*2.5+z*30])
            cube([30, 100, 30]);
        }
    }
    
    for (y=[0, 1, 2]) {
            
        for (z=[0, 1, 2]) {
                
            translate([0, (y+1)*2.5+y*30, (z+1)*2.5+z*30])
            cube([100, 30, 30]);
        }
    }
    
    for (x=[0, 1, 2]) {
        
        for (y=[0, 1, 2]) {
                
            translate([(x+1)*2.5+x*30, (y+1)*2.5+y*30, 0])
            cube([30, 30, 100]);
        }
    }
}

// Positions

circle_(0, 0, 0);
circle_(1, 1, 1);
circle_(1, 1, 2);
circle_(2, 2, 2);

cross_(0, 1, 0);
cross_(0, 1, 2);
cross_(0, 2, 1);
cross_(2, 0, 1);