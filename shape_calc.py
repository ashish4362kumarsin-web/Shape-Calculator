
import time as t
import sys
import math
import derives as dvs


# Drivation of variable


#------------ Maths ----------

def part():
    def maths():
        def area():
            def dimension_2d():
                def a_rect():
                    try:
                        l = int(input("Enter Length: "))
                        b = int(input("Enter Breadth: "))
                        formula = l * b

                        print("\n//:Wait//")
                        print()
                        t.sleep(0.4)
                        print("Area =", formula)
                    except ValueError:
                        print("You cannot enter alphabets!")

                def a_square():
                    try:
                        s = int(input("Enter Side: "))
                        formula = s ** 2

                        print("\n//:Wait//")
                        print()
                        t.sleep(0.4)
                        print("Area =", formula)

                    except ValueError:
                        print("Invalid value!")

                def a_tri():
                    try:
                        b = int(input("Enter Base:   "))
                        h = int(input("Enter Height:   "))
                        formula = (b * h) / 2
                    
                        print("\n//:Wait//")
                        print()
                        t.sleep(0.4)
                        print("Area =", formula)
                
                    except ValueError:
                        print("Invalid value!")
              
                def a_parallelogram():
                    try:
                        b = int(input("Enter Base:   "))
                        h = int(input("Enter Height:   "))
                        formula = b * h
                    
                        print("\n//:Wait//")
                        print()
                        t.sleep(0.4)
                        print("Area =", formula)
          
                    except Exception:
                        print("Invalid!")
            
                def a_rhombus():
                    try:
                        d1 = int(input("Enter Diagonal1:   "))
                        d2 = int(input("Enter Diagonal2:   "))
                        formula = (d1 * d2) / 2
               
                        print("\n//:Wait//")
                        print()
                        t.sleep(0.4)
                        print("Area =", formula)
            
                    except Exception:
                        print("Invalid!")
                
                def a_trapezium():
                    try:
                        h = int(input("Enter height:   "))
                        a = int(input("Enter parallel side1:   "))
                        b = int(input("Enter paralll side2: :   "))
                        
                        formula = 1/2 * h * (a + b)
                        
                        print("\n//:Wait//")
                        print()
                        t.sleep(0.4)
                        print("Area =", formula)
                    
                    except Exception:
                        print("Invalid!")
                    
                def a_circle():
                    try:
                        def area():
                            try:
                                r = int(input("Enter radius:   "))
                                pie = math.pi()
                                formula = (pie * r) ** 2
                            
                                print("\n//:Wait//")
                            
                                print()
                                t.sleep(0.4)
                                print("Area =", formula)
                            
                            except Exception:
                                print("Invalid!")
                        
                        
                        def circumference():
                            try:
                                r = int(input("Enter radius:   "))
                                pie = 22/7
                                formula = 2 * (pie * r)
                                
                                print("\n//:Wait//")
                                print()
                                t.sleep(0.4)
                                print("Circumference =", formula)
                            
                            except Exception:
                                print("Invalid!")
                            
                        
                        dvs.cir_a_c_entrance()
                        while True:
                            try:
                                print()
                                print("Press b to back!")
                                                                                       
                                choice = input("Enter Choice: ").strip().lower()
                                                                               
                                # Back option
                                if choice == "b":
                                    print("You are now on the previous page.")
                                    break
                                                                               
                                # Convert to integer only after checking b
                                choice = int(choice)
                                                                               
                                print()

                                if choice == 1:
                                    area()
                                elif choice == 2:
                                    circumference()
                                elif choice == 0:
                                    sys.exit(0)
                            
                            except Exception:
                                print("Invalid!")
                            
                    except Exception:
                        print("Invalid!")
                
                def a_semi_circle():
                    try:
                        def area():
                            try:
                                r = int(input("Enter radius:   "))
                                pie = math.pi()
                                formula = ((pie * r) ** 2)/2
                            
                                print("\n//:Wait//")
                            
                                print()
                                t.sleep(0.4)
                                print("Area =", formula)
                            
                            except Exception:
                                print("Invalid!")
                        
                        
                        def circumference():
                            try:
                                r = int(input("Enter radius:   "))
                                pie = 22/7
                                formula = (2 * (pie * r))/2
                                
                                print("\n//:Wait//")
                                print()
                                t.sleep(0.4)
                                print("Circumference =", formula)
                            
                            except Exception:
                                print("Invalid!")
                            
                        
                        dvs.cir_a_c_entrance()
                        while True:
                            try:
                                print()
                                print("Press b to back!")
                                                       
                                choice = input("Enter Choice: ").strip().lower()
                                               
                                # Back option
                                if choice == "b":
                                    print("You are now on the previous page.")
                                    break
                                               
                                # Convert to integer only after checking b
                                choice = int(choice)
                                               
                                print()

                                if choice == 1:
                                    area()
                                elif choice == 2:
                                    circumference()
                                elif choice == 0:
                                    sys.exit(0)
    
                            except Exception:
                                print("Invalid!")
                                
                    except Exception:
                        print("Invalid")


                dvs.a_dim_2d()
                while True:
                    try:
                        print()
                        print("Press b to back!")
                                                       
                        choice = input("Enter Choice: ").strip().lower()
                                               
                        # Back option
                        if choice == "b":
                            print("You are now on the previous page.")
                            break
                                               
                        # Convert to integer only after checking b
                        choice = int(choice)
                                               
                        print()

                        if choice == 1:
                            a_tri()
                        elif choice == 2:
                            a_rect()
                        elif choice == 3:
                            a_square()
                        elif choice == 4:
                            a_parallelogram()
                        elif choice == 5:
                            a_rhombus()
                        elif choice == 6:
                            a_trapezium
                        elif choice == 7:
                            a_circle()
                        elif choice == 8:
                            a_semi_circle()
                        elif choice == 0:
                            sys.exit(0)
                         
                        else:
                            print("Invalid Choice!")

                    except ValueError:
                        print("Error! Invalid choice")
      
            def dimension_3d():
                def a_cube():
                    def tsa():
                        try:
                            a = int(input("Enter Edge:   "))
                            formula = 6 * a ** 2
            
                            print("\n//:Wait//")
                            print()
                            t.sleep(0.4)
                            print("Area =", formula)
            
                        except Exception:
                            print("Invalid!") 
          
                    def lsa():
                        try:
                            a = int(input("Enter Edge:   "))
                            formula = 4 * a ** 2
            
                            print("\n//:Wait//")
                            print()
                            t.sleep(0.4)
                            print("Area =", formula)
            
                        except Exception:
                            print("Invalid!")    


          
                    dvs.a_dim_tsa_lsa()  # called
                    while True:
                        try:
                            print()
                            print("Press b to back!")
                                                       
                            choice = input("Enter Choice: ").strip().lower()
                                               
                            # Back option
                            if choice == "b":
                                print("You are now on the previous page.")
                                break
                                               
                            # Convert to integer only after checking b
                            choice = int(choice)
                                               
                            print()

                            if choice == 1:
                                tsa()
                            elif choice == 2:
                                lsa()
                            elif choice == 0:
                                sys.exit(0)

                        except Exception:
                            print("Invalid!")
                
                def a_cuboid():
                    def tsa():
                        try:
                            h = int(input("Enter Height:   "))
                            l = int(input("Enter length:   "))
                            b = int(input("Enter breadth:   "))
                            
                            formula = 2*((l*b) + (l*h) + (b*h))
            
                            print("\n//:Wait//")
                            print()
                            t.sleep(0.4)
                            print("Area =", formula)
            
                        except Exception:
                            print("Invalid!") 
          
                    def lsa():
                        try:
                            h = int(input("Enter Height:   "))
                            l = int(input("Enter length:   "))
                            b = int(input("Enter breadth:   "))
                            
                            formula = 2*h*(l + b)
            
                            print("\n//:Wait//")
                            print()
                            t.sleep(0.4)
                            print("Area =", formula)
            
                        except Exception:
                            print("Invalid!")    

          
                    dvs.a_dim_tsa_lsa()
                    while True:
                        try:
                            print()
                            print("Press b to back!")
                                                                                   
                            choice = input("Enter Choice: ").strip().lower()
                                                                           
                            # Back option
                            if choice == "b":
                                print("You are now on the previous page.")
                                break
                                                                           
                            # Convert to integer only after checking b
                            choice = int(choice)
                                                                           
                            print()
              
                            if choice == 1:
                                tsa()
                            elif choice == 2:
                                lsa()
                            elif choice == 0:
                                sys.exit(0)
                        
                        except Exception:
                            print("Invalid!")
                            
                def a_cylinder():
                    def tsa():
                        try:
                            h = int(input("Enter Height:   "))
                            r = int(input("Enter radius:   "))
                            
                            pie = 22/7
                            formula = 2*pie*r*(r + h)
            
                            print("\n//:Wait//")
                            print()
                            t.sleep(0.4)
                            print("Area =", formula)
            
                        except Exception:
                            print("Invalid!") 
          
                    def lsa():
                        try:
                            h = int(input("Enter Height:   "))
                            r = int(input("Enter radius:   "))
                         
                            pie = 22/7
                            formula = 2*pie*r*h
            
                            print("\n//:Wait//")
                            print()
                            t.sleep(0.4)
                            print("Area =", formula)
            
                        except Exception:
                            print("Invalid!")    


                    dvs.a_dim_tsa_lsa()  # called
                    while True:
                        try:
                            print()
                            print("Press b to back!")
                                                       
                            choice = input("Enter Choice: ").strip().lower()
                                               
                            # Back option
                            if choice == "b":
                                print("You are now on the previous page.")
                                break
                                               
                            # Convert to integer only after checking b
                            choice = int(choice)
                                               
                            print()

                            if choice == 1:
                                tsa()
                            elif choice == 2:
                                lsa()
                            elif choice == 0:
                                sys.exit(0)
                            
                        except Exception:
                            print("Invalid!")
                
                def a_cone():
                    def tsa():
                        try:
                            r = int(input("Enter radius:   "))
                            l = int(input("Enter length:   "))
                            
                            pie = 22/7
                            formula = pie*r*(r + l)
            
                            print("\n//:Wait//")
                            print()
                            t.sleep(0.4)
                            print("Area =", formula)
            
                        except Exception:
                            print("Invalid!") 
          
                    def lsa():
                        try:
                            r = int(input("Enter radius:   "))
                            l = int(input("Enter length:   "))
                            
                            pie = 22/7
                            formula = pie*r*l
            
                            print("\n//:Wait//")
                            print()
                            t.sleep(0.4)
                            print("Area =", formula)
            
                        except Exception:
                            print("Invalid!")    

          
                    dvs.a_dim_tsa_lsa()  # called
                    while True:
                        try:
                            print()
                            print("Press b to back!")
                                                       
                            choice = input("Enter Choice: ").strip().lower()
                                               
                            # Back option
                            if choice == "b":
                                print("You are now on the previous page.")
                                break
                                               
                            # Convert to integer only after checking b
                            choice = int(choice)
                                               
                            print()
              
                            if choice == 1:
                                tsa()
                            elif choice == 2:
                                lsa()
                            elif choice == 0:
                                sys.exit(0)
                        
                        except Exception:
                            print("Invalid!")
                
                def a_sphere():
                    try:
                        r = int(input("Enter radius:   "))
                        print()
                        print("TSA = LSA, So there is no specific TSA or LSA of Spheres.")
                        
                        pie = math.pi()
                        formula = 4 * (pie * (r ** 2))
                        
                        print("\n//:Wait//")
                        print()
                        t.sleep(0.4)
                        print("Area =", formula)
            
                    except Exception:
                        print("Invalid!") 
                
                def a_hemisphere():
                    def tsa():
                        try:
                            r = int(input("Enter radius:   "))
                                                
                            pie = math.pi()
                            formula = 3 * (pie * (r ** 2))
                                
                            print("\n//:Wait//")
                            print()
                            t.sleep(0.4)
                            print("Area =", formula)
                                
                        except Exception:
                            print("Invalid!") 
                              
                    def lsa():
                        try:
                            r = int(input("Enter radius:   "))
                                                
                            pie = math.pi()
                            formula = 2 * (pie * (r ** 2))
                                
                            print("\n//:Wait//")
                            print()
                            t.sleep(0.4)
                            print("Area =", formula)
                                
                        except Exception:
                            print("Invalid!")    

                              
                    dvs.a_dim_tsa_lsa()  # called
                    while True:
                        try:
                            print()
                            print("Press b to back!")
                                                       
                            choice = input("Enter Choice: ").strip().lower()
                                               
                            # Back option
                            if choice == "b":
                                print("You are now on the previous page.")
                                break
                                               
                            # Convert to integer only after checking b
                            choice = int(choice)
                                               
                            print()

                            if choice == 1:
                                tsa()
                            elif choice == 2:
                                lsa()
                            elif choice == 0:
                                sys.exit(0)
                                            
                        except Exception:
                            print("Invalid!")
                        
                dvs.a_dim_3d()

                while True:
                    try:
                        print()
                        print("Press b to back!")
                                                   
                        choice = input("Enter Choice: ").strip().lower()
                                           
                        # Back option
                        if choice == "b":
                            print("You are now on the previous page.")
                            break
                                           
                        # Convert to integer only after checking b
                        choice = int(choice)
                                           
                        print()
                
                        if choice == 1:
                            a_cube()
                        elif choice == 2:
                            a_cuboid()
                        elif choice == 3:
                            a_cylinder()
                        elif choice == 4:
                            a_cone()
                        elif choice == 5:
                            a_sphere()
                        elif choice == 6:
                            a_hemisphere()
                        elif choice == 0:
                            sys.exit(0)
                        
                    except Exception:
                        print("Invalid!")
            
            dvs.a_dimension_entrance()
            
            while True:
                try:
                    print()
                    print("Press b to back!")
                            
                    choice = input("Enter Choice: ").strip().lower()
                    
                    # Back option
                    if choice == "b":
                        print("You are now on the previous page.")
                        break
                    
                    # Convert to integer only after checking b
                    choice = int(choice)
                    
                    print()
                    
                    if choice == 1:
                        dimension_2d()
                    elif choice == 2:
                        dimension_3d()
                    elif choice == 0:
                        sys.exit(0)
                
                except Exception:
                    print("Invalid!")
                    
        def volume():
            def v_cube():
                try:
                    a = int(input("Enter Side:"))
                    
                    formula = a ** 3
                    
                    print("\n//:Wait//")
                    print()
                    t.sleep(0.4)
                    print("Area =", formula)
                    
                except Exception:
                    print("Invalid!")
            
            def v_cuboid():
                try:
                    l = int(input("Enter Length:   "))
                    b = int(input("Enter Breadth:   "))
                    h = int(input("Enter Height:   "))
                    
                    formula = l * b * h 
                    
                    print("\n//:Wait//")
                    print()
                    t.sleep(0.4)
                    print("Area =", formula)
                
                except Exception:
                    print("Invalid!")
            
            def v_cylinder():
                try:
                    r = int(input("Enter Radius:   "))
                    h = int(input("Enter Height:   "))
                    
                    pie = 22/7
                    formula = pie * (r ** 2) * h
                    
                    print("\n//:Wait//")
                    print()
                    t.sleep(0.4)
                    print("Area =", formula)
                    
                except Exception:
                    print("Invalid!")
                    
            def v_cone():
                try:
                    r = int(input("Enter Radius:   "))
                    h = int(input("Enter Height:   "))
                    
                    pie = 22/7
                    formula = 1/3 * (pie * (r **2) * h)
                    
                    print("\n//:Wait//")
                    print()
                    t.sleep(0.4)
                    print("Area =", formula)
                
                except Exception:
                    print("Invalid!")
                    
            def v_sphere():
                try:
                    r = int(input("Enter Radius:   "))
                    
                    pie = 22/7
                    formula = 4/3 * (pie * (r **3))
                    
                    print("\n//:Wait//")
                    print()
                    t.sleep(0.4)
                    print("Area =", formula)
                
                except Exception:
                    print("Invalid!")
            
            def v_hemisphere():
                try:
                    r = int(input("Enter Radius:   "))
                    
                    pie = 22/7
                    formula = 2/3 * (pie * (r ** 3))
                    
                    print("\n//:Wait//")
                    print()
                    t.sleep(0.4)
                    print("Area =", formula)
                
                except Exception:
                    print("Invalid!")

                    
            dvs.v_shapes_entrance()
            while True:
                try:
                    print()
                    print("Press b to back!")
                            
                    choice = input("Enter Choice: ").strip().lower()
                    
                    # Back option
                    if choice == "b":
                        print("You are now on the previous page.")
                        break
                    
                    # Convert to integer only after checking b
                    choice = int(choice)
                    
                    print()

                    if choice == 1:
                        v_cube()
                    elif choice == 2:
                        v_cuboid()
                    elif choice == 3:
                        v_cylinder()
                    elif choice == 4:
                        v_cone()
                    elif choice == 5:
                        v_sphere()
                    elif choice == 6:
                        v_hemisphere()
                    elif choice == 0:
                        sys.exit(0)
                except Exception:
                    print("Invalid!")
        
        dvs.a_v_entrance()
        while True:
            try:
                print()
                print("Press b to back!")
        
                choice = input("Enter Choice: ").strip().lower()
                

                # Back option
                if choice == "b":
                    print("You are now on the previous page.")
                    break

                # Convert to integer only after checking b
                choice = int(choice)

                print()

                if choice == 1:
                    area()
                elif choice == 2:
                    volume()
                elif choice == 0:
                    sys.exit(0)
                else:
                    print("Invalid choice!")
            
            except Exception:
                print("Invalid!")
# ------------ Main Menu ------------#


    dvs.main_entrance()

    while True:
        try:
            print()
            choice = int(input("Enter Choice:    "))
            print()
        
            if choice == 1:
                maths()
            elif choice == 0:
                sys.exit(0)
            else:
                print("Invalid!")
    
        except ValueError:
            print("Invalid!")
            
        except EOFError:
            print("No input detected!")
            sys.exit(0)

if __name__ == '__main__':
    part()