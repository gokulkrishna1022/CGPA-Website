from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    v = "no"  # Default value
    if request.method == 'POST':
        v = request.form.get('hm')
    return render_template('index.html',v=v)

@app.route('/calculate', methods=['POST'])
def calculate():
    v = request.form['hm']
    f1 = request.form['semester']
    
    result = ""

    if f1 == "4":
        result = calculate_gpa_semester_4(request.form, v)
    elif f1 == "5":
        result = calculate_gpa_semester_5(request.form, v)
    elif f1 == "6":
        result = calculate_gpa_semester_6(request.form, v)  
    elif f1 == "total":
        result = calculate_total_cgpa(request.form, v )   
    elif f1 == "1":
        result = calculate_gpa_semester_1(request.form, v)   
    elif f1 == "2":
        result = calculate_gpa_semester_2(request.form, v)
    elif f1 == "3":
        result = calculate_gpa_semester_3(request.form, v)
    elif f1 == "7":
        result = calculate_gpa_semester_7(request.form, v) 
    elif f1 == "8":
        result = calculate_gpa_semester_8(request.form, v)                    

    return render_template('index.html', result=result, v=v)


def calculate_gpa_semester_1(form_data, v):
    # Initialize grade values 
    if v == "yes":
        h1 = form_data['mathematics_1']
        h2 = form_data['basic_electrical_engineering']
        h3 = form_data['programming_for_problem_Solvings']
        h4 = form_data['engineering_graphics_and_computer_aided_drawing']
        h5 = form_data['electrical_engineering_laboratory']
        h6 = form_data['programming_laboratory']
    
    
        i = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i[1] = grade(i[1], h1)
        i[1] = i[1] * 4
        i[2] = grade(i[2], h2)
        i[2] = i[2] * 4
        i[3] = grade(i[3], h3)
        i[3] = i[3] * 3
        i[4] = grade(i[4], h4)
        i[4] = i[4] * 3
        i[5] = grade(i[5], h5)
        i[5] = i[5] * 1.5
        i[6] = grade(i[6], h6)
        i[6] = i[6] * 1.5
    
        total_weighted_grade_points = sum(i)
        total_credits = 17
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for First Semester : {:.2f}".format(gpa)
    else:
        h1 = form_data['mathematics_1']
        h2 = form_data['basic_electrical_engineering']
        h3 = form_data['programming_for_problem_Solvings']
        h4 = form_data['engineering_graphics_and_computer_aided_drawing']
        h5 = form_data['electrical_engineering_laboratory']
        h6 = form_data['programming_laboratory']
    
    
        i = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i[1] = grade(i[1], h1)
        i[1] = i[1] * 4
        i[2] = grade(i[2], h2)
        i[2] = i[2] * 4
        i[3] = grade(i[3], h3)
        i[3] = i[3] * 3
        i[4] = grade(i[4], h4)
        i[4] = i[4] * 3
        i[5] = grade(i[5], h5)
        i[5] = i[5] * 1.5
        i[6] = grade(i[6], h6)
        i[6] = i[6] * 1.5
    
        total_weighted_grade_points = sum(i)
        total_credits = 17
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for First Semester : {:.2f}".format(gpa)  
    return result      

def calculate_gpa_semester_2(form_data, v):
    # Initialize grade values 
    if v == "yes":
        j1 = form_data['mathematics_2']
        j2 = form_data['physics']
        j3 = form_data['chemistry']
        j4 = form_data['english_for_communication']
        j5 = form_data['Workshop_and_manufacturing_practice']
        j6 = form_data['physics_laboratory']
        j7 = form_data['chemistry_laboratory']
    
    
        k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        k[1] = grade(k[1], j1)
        k[1] = k[1] * 4
        k[2] = grade(k[2], j2)
        k[2] = k[2] * 4
        k[3] = grade(k[3], j3)
        k[3] = k[3] * 4
        k[4] = grade(k[4], j4)
        k[4] = k[4] * 3
        k[5] = grade(k[5], j5)
        k[5] = k[5] * 1.5
        k[6] = grade(k[6], j6)
        k[6] = k[6] * 1.5
        k[7] = grade(k[7], j7)
        k[7] = k[7] * 1.5
    
        total_weighted_grade_points = sum(k)
        total_credits = 19.5
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for Second Semester : {:.2f}".format(gpa)
    else:
        j1 = form_data['mathematics_2']
        j2 = form_data['physics']
        j3 = form_data['chemistry']
        j4 = form_data['english_for_communication']
        j5 = form_data['Workshop_and_manufacturing_practice']
        j6 = form_data['physics_laboratory']
        j7 = form_data['chemistry_laboratory']
    
    
        k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        k[1] = grade(k[1], j1)
        k[1] = k[1] * 4
        k[2] = grade(k[2], j2)
        k[2] = k[2] * 4
        k[3] = grade(k[3], j3)
        k[3] = k[3] * 4
        k[4] = grade(k[4], j4)
        k[4] = k[4] * 3
        k[5] = grade(k[5], j5)
        k[5] = k[5] * 1.5
        k[6] = grade(k[6], j6)
        k[6] = k[6] * 1.5
        k[7] = grade(k[7], j7)
        k[7] = k[7] * 1.5
    
        total_weighted_grade_points = sum(k)
        total_credits = 19.5
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for Second Semester : {:.2f}".format(gpa)
    return result    


def calculate_gpa_semester_3(form_data, v):
    # Initialize grade values 
    if v == "yes":
        l1 = form_data['linear_algebra']
        l2 = form_data['Circuits_and_networks']
        l3 = form_data['Electronic_devices_and_circuits']
        l4 = form_data['Electromagnetic_waves_and_fields']
        l5 = form_data['Digital_system_design']
        l6 = form_data['Data_structures']
        l7 = form_data['Electronic_devices']
        l8 = form_data['Data_structures_lab']
        l9 = form_data['Semiconductor_technology']
    
    # Calculate GPA for fourth semester
        m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        m[1] = grade(m[1], l1)
        m[1] = m[1] * 4
        m[2] = grade(m[2], l2)
        m[2] = m[2] * 3
        m[3] = grade(m[3], l3)
        m[3] = m[3] * 3
        m[4] = grade(m[4], l4)
        m[4] = m[4] * 3
        m[5] = grade(m[5], l5)
        m[5] = m[5] * 3
        m[6] = grade(m[6], l6)
        m[6] = m[6] * 3
        m[7] = grade(m[7], l7)
        m[7] = m[7] * 1.5
        m[8] = grade(m[8], l8)
        m[8] = m[8] * 1.5
        m[9] = grade(m[9], l9)
        m[9] = m[9] * 4
    
        total_weighted_grade_points = sum(m)
        total_credits = 26
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for Third Semester : {:.2f}".format(gpa)
    else:
        l1 = form_data['linear_algebra']
        l2 = form_data['Circuits_and_networks']
        l3 = form_data['Electronic_devices_and_circuits']
        l4 = form_data['Electromagnetic_waves_and_fields']
        l5 = form_data['Digital_system_design']
        l6 = form_data['Data_structures']
        l7 = form_data['Electronic_devices']
        l8 = form_data['Data_structures_lab']
        
    
    # Calculate GPA for fourth semester
        m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        m[1] = grade(m[1], l1)
        m[1] = m[1] * 4
        m[2] = grade(m[2], l2)
        m[2] = m[2] * 3
        m[3] = grade(m[3], l3)
        m[3] = m[3] * 3
        m[4] = grade(m[4], l4)
        m[4] = m[4] * 3
        m[5] = grade(m[5], l5)
        m[5] = m[5] * 3
        m[6] = grade(m[6], l6)
        m[6] = m[6] * 3
        m[7] = grade(m[7], l7)
        m[7] = m[7] * 1.5
        m[8] = grade(m[8], l8)
        m[8] = m[8] * 1.5
        
    
        total_weighted_grade_points = sum(m)
        total_credits = 22
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for Third Semester : {:.2f}".format(gpa)

    return result



def calculate_gpa_semester_4(form_data, v):
    # Initialize grade values 
    if v == "yes":
        e1 = form_data['transmission_lines']
        e2 = form_data['electronic_circuit_design']
        e3 = form_data['signals_and_systems']
        e4 = form_data['analog_communication']
        e5 = form_data['computer_architecture']
        e6 = form_data['biology_for_engineers']
        e7 = form_data['digital_system_design_lab']
        e8 = form_data['electronic_circuit_design_lab']
        e9 = form_data['analog_communication_lab']
        e10 = form_data['medical_electronics_and_informatics']
    
    # Calculate GPA for fourth semester
        c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        c[1] = grade(c[1], e1)
        c[1] = c[1] * 3
        c[2] = grade(c[2], e2)
        c[2] = c[2] * 3
        c[3] = grade(c[3], e3)
        c[3] = c[3] * 4
        c[4] = grade(c[4], e4)
        c[4] = c[4] * 3
        c[5] = grade(c[5], e5)
        c[5] = c[5] * 3
        c[6] = grade(c[6], e6)
        c[6] = c[6] * 2
        c[7] = grade(c[7], e7)
        c[7] = c[7] * 1.5
        c[8] = grade(c[8], e8)
        c[8] = c[8] * 1.5
        c[9] = grade(c[9], e9)
        c[9] = c[9] * 1.5
        c[10] = grade(c[10], e10)
        c[10] = c[10] * 4
    
        total_weighted_grade_points = sum(c)
        total_credits = 26.5
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for Fourth Semester : {:.2f}".format(gpa)
    else:
        e1 = form_data['transmission_lines']
        e2 = form_data['electronic_circuit_design']
        e3 = form_data['signals_and_systems']
        e4 = form_data['analog_communication']
        e5 = form_data['computer_architecture']
        e6 = form_data['biology_for_engineers']
        e7 = form_data['digital_system_design_lab']
        e8 = form_data['electronic_circuit_design_lab']
        e9 = form_data['analog_communication_lab']
        
    
    # Calculate GPA for fourth semester
        c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        c[1] = grade(c[1], e1)
        c[1] = c[1] * 3
        c[2] = grade(c[2], e2)
        c[2] = c[2] * 3
        c[3] = grade(c[3], e3)
        c[3] = c[3] * 4
        c[4] = grade(c[4], e4)
        c[4] = c[4] * 3
        c[5] = grade(c[5], e5)
        c[5] = c[5] * 3
        c[6] = grade(c[6], e6)
        c[6] = c[6] * 2
        c[7] = grade(c[7], e7)
        c[7] = c[7] * 1.5
        c[8] = grade(c[8], e8)
        c[8] = c[8] * 1.5
        c[9] = grade(c[9], e9)
        c[9] = c[9] * 1.5
    
        total_weighted_grade_points = sum(c)
        total_credits = 22.5
        gpa = total_weighted_grade_points / total_credits
        result = "Your GPA for Fourth Semester : {:.2f}".format(gpa)

    return result


def calculate_gpa_semester_5(form_data, v):

    

    if v == "yes":
        g1 = form_data['digital_signal_processing']
        g2 = form_data['digital_communication']
        g3 = form_data['microprocessors_microcontrollers']
        g4 = form_data['entrepreneurship']
        g5 = form_data['antennas_wave_propagation']
        g6 = form_data['oec']
        g7 = form_data['digital_signal_processing_lab']
        g8 = form_data['digital_communication_lab']
        g9 = form_data['microprocessors_microcontrollers_lab']
        g10 = form_data['advanced_digital_system_design']

    # Calculate GPA for fifth semester
        d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        d[1] = grade(d[1], g1)
        d[1] = d[1] * 4
        d[2] = grade(d[2], g2)
        d[2] = d[2] * 3
        d[3] = grade(d[3], g3)
        d[3] = d[3] * 3
        d[4] = grade(d[4], g4)
        d[4] = d[4] * 2
        d[5] = grade(d[5], g5)
        d[5] = d[5] * 3
        d[6] = grade(d[6], g6)
        d[6] = d[6] * 3
        d[7] = grade(d[7], g7)
        d[7] = d[7] * 1.5
        d[8] = grade(d[8], g8)
        d[8] = d[8] * 1.5
        d[9] = grade(d[9], g9)
        d[9] = d[9] * 1.5
        d[10] = grade(d[10], g10)
        d[10] = d[10] * 4

        total_weighted_grade_points = sum(d)
        total_credits = 26.5
        gpa = total_weighted_grade_points / total_credits
        result = "Your GPA for Fifth Semester: {:.2f}".format(gpa)
    else:
        g1 = form_data['digital_signal_processing']
        g2 = form_data['digital_communication']
        g3 = form_data['microprocessors_microcontrollers']
        g4 = form_data['entrepreneurship']
        g5 = form_data['antennas_wave_propagation']
        g6 = form_data['oec']
        g7 = form_data['digital_signal_processing_lab']
        g8 = form_data['digital_communication_lab']
        g9 = form_data['microprocessors_microcontrollers_lab']
        
    # Calculate GPA for fifth semester
        d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        d[1] = grade(d[1], g1)
        d[1] = d[1] * 4
        d[2] = grade(d[2], g2)
        d[2] = d[2] * 3
        d[3] = grade(d[3], g3)
        d[3] = d[3] * 3
        d[4] = grade(d[4], g4)
        d[4] = d[4] * 2
        d[5] = grade(d[5], g5)
        d[5] = d[5] * 3
        d[6] = grade(d[6], g6)
        d[6] = d[6] * 3
        d[7] = grade(d[7], g7)
        d[7] = d[7] * 1.5
        d[8] = grade(d[8], g8)
        d[8] = d[8] * 1.5
        d[9] = grade(d[9], g9)
        d[9] = d[9] * 1.5
    
        total_weighted_grade_points = sum(d)
        total_credits = 22.5
        gpa = total_weighted_grade_points / total_credits
        result = "Your GPA for Fifth Semester: {:.2f}".format(gpa)

    return result



def calculate_gpa_semester_6(form_data, v):
    # Initialize grade values
    if v == "yes":
        a1 = form_data['microwave_optical_engineering']
        w = form_data['data_communication_networks']
        x = form_data['vlsi_design']
        y = form_data['control_systems_engineering']
        z = form_data['industrial_management_economics']
        f = form_data['oec_sixth']
        g = form_data['microwave_optical_engineering_lab']
        h = form_data['vlsi_design_lab']
        i = form_data['data_communication_networks_lab']
        j = form_data['simulation_communication_systems']

    # Calculate GPA for sixth semester
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        b[1] = grade(b[1], a1)
        b[1] = b[1] * 3
        b[2] = grade(b[2], w)
        b[2] = b[2] * 3
        b[3] = grade(b[3], x)
        b[3] = b[3] * 3
        b[4] = grade(b[4], y)
        b[4] = b[4] * 3
        b[5] = grade(b[5], z)
        b[5] = b[5] * 3
        b[6] = grade(b[6], f)
        b[6] = b[6] * 3
        b[7] = grade(b[7], g)
        b[7] = b[7] * 1.5
        b[8] = grade(b[8], h)
        b[8] = b[8] * 1.5
        b[9] = grade(b[9], i)
        b[9] = b[9] * 1.5
        b[10] = grade(b[10], j)
        b[10] = b[10] * 4

        total_weighted_grade_points = sum(b)
        total_credits = 26.5
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for Sixth Semester : {:.2f}".format(gpa)
    else:
        a1 = form_data['microwave_optical_engineering']
        w = form_data['data_communication_networks']
        x = form_data['vlsi_design']
        y = form_data['control_systems_engineering']
        z = form_data['industrial_management_economics']
        f = form_data['oec_sixth']
        g = form_data['microwave_optical_engineering_lab']
        h = form_data['vlsi_design_lab']
        i = form_data['data_communication_networks_lab']

    # Calculate GPA for sixth semester
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        b[1] = grade(b[1], a1)
        b[1] = b[1] * 3
        b[2] = grade(b[2], w)
        b[2] = b[2] * 3
        b[3] = grade(b[3], x)
        b[3] = b[3] * 3
        b[4] = grade(b[4], y)
        b[4] = b[4] * 3
        b[5] = grade(b[5], z)
        b[5] = b[5] * 3
        b[6] = grade(b[6], f)
        b[6] = b[6] * 3
        b[7] = grade(b[7], g)
        b[7] = b[7] * 1.5
        b[8] = grade(b[8], h)
        b[8] = b[8] * 1.5
        b[9] = grade(b[9], i)
        b[9] = b[9] * 1.5
    
        total_weighted_grade_points = sum(b)
        total_credits = 22.5

        gpa = total_weighted_grade_points / total_credits
        result = "Your GPA for Sixth Semester : {:.2f}".format(gpa)

    return result

def calculate_gpa_semester_7(form_data, v):
    # Initialize grade values
    if v == "yes":
        n1 = form_data['Wireless_communication']
        n2 = form_data['Information_theory_and_coding']
        n3 = form_data['Embedded_system']
        n4= form_data['Cryptography_and_network_Security']
        n5 = form_data['Internet_of_everything']
        n6 = form_data['Wireless_communication_laboratory']
        n7 = form_data['Embedded_system_laboratory']
        n8 = form_data['Mini_project']
        n9 = form_data['Next_generation_networks']
        

    # Calculate GPA for sixth semester
        o = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        o[1] = grade(o[1], n1)
        o[1] = o[1] * 3
        o[2] = grade(o[2], n2)
        o[2] = o[2] * 3
        o[3] = grade(o[3], n3)
        o[3] = o[3] * 3
        o[4] = grade(o[4], n4)
        o[4] = o[4] * 3
        o[5] = grade(o[5], n5)
        o[5] = o[5] * 3
        o[6] = grade(o[6], n6)
        o[6] = o[6] * 1.5
        o[7] = grade(o[7], n7)
        o[7] = o[7] * 1.5
        o[8] = grade(o[8], n8)
        o[8] = o[8] * 1
        o[9] = grade(o[9], n9)
        o[9] = o[9] * 4

        total_weighted_grade_points = sum(o)
        total_credits = 23
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for Seventh Semester : {:.2f}".format(gpa)
    else:
        n1 = form_data['Wireless_communication']
        n2 = form_data['Information_theory_and_coding']
        n3 = form_data['Embedded_system']
        n4= form_data['Cryptography_and_network_Security']
        n5 = form_data['Internet_of_everything']
        n6 = form_data['Wireless_communication_laboratory']
        n7 = form_data['Embedded_system_laboratory']
        n8 = form_data['Mini_project']
        

    # Calculate GPA for sixth semester
        o = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        o[1] = grade(o[1], n1)
        o[1] = o[1] * 3
        o[2] = grade(o[2], n2)
        o[2] = o[2] * 3
        o[3] = grade(o[3], n3)
        o[3] = o[3] * 3
        o[4] = grade(o[4], n4)
        o[4] = o[4] * 3
        o[5] = grade(o[5], n5)
        o[5] = o[5] * 3
        o[6] = grade(o[6], n6)
        o[6] = o[6] * 1.5
        o[7] = grade(o[7], n7)
        o[7] = o[7] * 1.5
        o[8] = grade(o[8], n8)
        o[8] = o[8] * 1

        total_weighted_grade_points = sum(o)
        total_credits = 19
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for Seventh Semester : {:.2f}".format(gpa)

    return result

def calculate_gpa_semester_8(form_data, v):
    # Initialize grade values 
    if v == "yes":
        p1 = form_data['swayam_1']
        p2 = form_data['swayam_2']
        p3 = form_data['Comprehensive_test']
        p4 = form_data['Internship']
        p5 = form_data['Project_work']
    
    
        q = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        q[1] = grade(q[1], p1)
        q[1] = q[1] * 2
        q[2] = grade(q[2], p2)
        q[2] = q[2] * 2
        q[3] = grade(q[3], p3)
        q[3] = q[3] * 1
        q[4] = grade(q[4], p4)
        q[4] = q[4] * 2
        q[5] = grade(q[5], p5)
        q[5] = q[5] * 8
    
        total_weighted_grade_points = sum(q)
        total_credits = 15
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for First Semester : {:.2f}".format(gpa)
    else:
        p1 = form_data['swayam_1']
        p2 = form_data['swayam_2']
        p3 = form_data['Comprehensive_test']
        p4 = form_data['Internship']
        p5 = form_data['Project_work']
    
    
        q = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        q[1] = grade(q[1], p1)
        q[1] = q[1] * 2
        q[2] = grade(q[2], p2)
        q[2] = q[2] * 2
        q[3] = grade(q[3], p3)
        q[3] = q[3] * 1
        q[4] = grade(q[4], p4)
        q[4] = q[4] * 2
        q[5] = grade(q[5], p5)
        q[5] = q[5] * 8
    
        total_weighted_grade_points = sum(q)
        total_credits = 15
        gpa = total_weighted_grade_points /total_credits
        result = "Your GPA for First Semester : {:.2f}".format(gpa)  
    return result 






def calculate_total_cgpa(form_data, v):
    f2 = request.form['completed_semester']
    if v == "yes":
        if f2 == "2":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            total_cgpa=(((first_sem_gpa)*17) + ((second_sem_gpa)*19.5))/36.5
        elif f2 == "3":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])    
            total_cgpa=(((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*26))/62.5
        elif f2 == "4":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])
            fourth_sem_gpa = float(form_data['fourth_sem_gpa'])
            total_cgpa=(((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*26) +((fourth_sem_gpa)*26.5))/89
        elif f2 == "5":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])
            fourth_sem_gpa = float(form_data['fourth_sem_gpa'])
            fifth_sem_gpa = float(form_data['fifth_sem_gpa']) 
            total_cgpa= (((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*26) +((fourth_sem_gpa)*26.5) + ((fifth_sem_gpa)*26.5))/115.5
        elif f2 =="6":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])
            fourth_sem_gpa = float(form_data['fourth_sem_gpa'])
            fifth_sem_gpa = float(form_data['fifth_sem_gpa'])
            sixth_sem_gpa = float(form_data['sixth_sem_gpa'])
            total_weighted_gpa = (((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*26) +((fourth_sem_gpa)*26.5) + ((fifth_sem_gpa)*26.5) + ((sixth_sem_gpa)*26.5))
            total_cgpa = total_weighted_gpa / 142    # Updated the total credits for "yes"
        elif f2 =="7":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])
            fourth_sem_gpa = float(form_data['fourth_sem_gpa'])
            fifth_sem_gpa = float(form_data['fifth_sem_gpa'])
            sixth_sem_gpa = float(form_data['sixth_sem_gpa'])
            seventh_sem_gpa = float(form_data['seventh_sem_gpa'])
            
            total_weighted_gpa = (((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*26) +((fourth_sem_gpa)*26.5) + ((fifth_sem_gpa)*26.5) + ((sixth_sem_gpa)*26.5)+((seventh_sem_gpa)*23))
            total_cgpa = total_weighted_gpa / 165
        elif f2 =="8":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])
            fourth_sem_gpa = float(form_data['fourth_sem_gpa'])
            fifth_sem_gpa = float(form_data['fifth_sem_gpa'])
            sixth_sem_gpa = float(form_data['sixth_sem_gpa'])
            seventh_sem_gpa = float(form_data['seventh_sem_gpa'])
            eighth_sem_gpa = float(form_data['seventh_sem_gpa'])
            total_weighted_gpa = (((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*26) +((fourth_sem_gpa)*26.5) + ((fifth_sem_gpa)*26.5) + ((sixth_sem_gpa)*26.5)+((seventh_sem_gpa)*23)+((eighth_sem_gpa)*15))
            total_cgpa = total_weighted_gpa / 180    
    
    else:
        if f2 == "2":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            total_cgpa=(((first_sem_gpa)*17) + ((second_sem_gpa)*19.5))/36.5
        elif f2 == "3":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])    
            total_cgpa=(((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*22))/58.5
        elif f2 == "4":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])
            fourth_sem_gpa = float(form_data['fourth_sem_gpa'])
            total_cgpa=(((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*22) +((fourth_sem_gpa)*22.5))/81
        elif f2 == "5":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])
            fourth_sem_gpa = float(form_data['fourth_sem_gpa'])
            fifth_sem_gpa = float(form_data['fifth_sem_gpa']) 
            total_cgpa= (((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*22) +((fourth_sem_gpa)*22.5) + ((fifth_sem_gpa)*22.5))/103.5
        elif f2 =="6":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])
            fourth_sem_gpa = float(form_data['fourth_sem_gpa'])
            fifth_sem_gpa = float(form_data['fifth_sem_gpa'])
            sixth_sem_gpa = float(form_data['sixth_sem_gpa'])
            total_weighted_gpa = (((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*22) +((fourth_sem_gpa)*22.5) + ((fifth_sem_gpa)*22.5) + ((sixth_sem_gpa)*22.5))
            total_cgpa = total_weighted_gpa / 126  # Updated the total credits for "no"
        elif f2 =="7":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])
            fourth_sem_gpa = float(form_data['fourth_sem_gpa'])
            fifth_sem_gpa = float(form_data['fifth_sem_gpa'])
            sixth_sem_gpa = float(form_data['sixth_sem_gpa'])
            seventh_sem_gpa = float(form_data['seventh_sem_gpa'])
            
            total_weighted_gpa = (((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*22) +((fourth_sem_gpa)*22.5) + ((fifth_sem_gpa)*22.5) + ((sixth_sem_gpa)*22.5)+((seventh_sem_gpa)*19))
            total_cgpa = total_weighted_gpa / 145
        elif f2 =="8":
            first_sem_gpa = float(form_data['first_sem_gpa'])
            second_sem_gpa = float(form_data['second_sem_gpa'])
            third_sem_gpa = float(form_data['third_sem_gpa'])
            fourth_sem_gpa = float(form_data['fourth_sem_gpa'])
            fifth_sem_gpa = float(form_data['fifth_sem_gpa'])
            sixth_sem_gpa = float(form_data['sixth_sem_gpa'])
            seventh_sem_gpa = float(form_data['seventh_sem_gpa'])
            eighth_sem_gpa = float(form_data['seventh_sem_gpa'])
            total_weighted_gpa = (((first_sem_gpa)*17) + ((second_sem_gpa)*19.5) + ((third_sem_gpa)*22) +((fourth_sem_gpa)*22.5) + ((fifth_sem_gpa)*22.5) + ((sixth_sem_gpa)*22.5)+((seventh_sem_gpa)*19)+((eighth_sem_gpa)*15))
            total_cgpa = total_weighted_gpa / 160     

    return "Your Total CGPA: {:.2f}".format(total_cgpa)




def grade(grade_value, subject_grade):
    if (subject_grade == "S" or subject_grade == "s"):
        grade_value = 10
    elif (subject_grade == "A" or subject_grade == "a") :
        grade_value = 9
    elif (subject_grade == "B" or subject_grade == "b"):
        grade_value = 8
    elif (subject_grade == "C" or subject_grade == "c"):
        grade_value = 7
    elif (subject_grade == "D" or subject_grade == "d"):
        grade_value = 6
    elif (subject_grade == "E" or subject_grade == "e") :
        grade_value = 5
    else:
        grade_value = 0
    
    return grade_value


if __name__ == '__main__':
    app.run(debug=True , port=5000)