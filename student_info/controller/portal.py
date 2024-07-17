from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.exceptions import ValidationError



class EnrollmentController(CustomerPortal):

    def _prepare_home_portal_values(self, counters):

        vals = super(EnrollmentController,self)._prepare_home_portal_values(counters)
        current_user = request.env.user
        enroll_obj = request.env['enrollment.form']


        if current_user.has_group('student_info.group_supervisor'):
            vals['enroll_count'] = enroll_obj.sudo().search_count([])
        else:
            vals['enroll_count'] = enroll_obj.sudo().search_count([('email', '=', current_user.email)])

        return vals
    
    # Enrollment Form Web page
    @http.route('/enrollment',auth='public',website=True)
    def enrollment_form(self,**kwargs):
        colleges = request.env['college.college'].sudo().search([])
        courses = request.env['course.course'].sudo().search([])
        return http.request.render('student_info.enrollment_submission_form',{
            'colleges':colleges,'courses':courses
        })
    
    #Submiting the Enrollment Form on website
    @http.route('/enrollment/submit_form',auth='public',website=True, type='http',csrf=True)
    def enrollment_submission(self,**kwargs):

        name = kwargs.get('name')
        phone = kwargs.get('phone')
        email = kwargs.get('email')
        dob = kwargs.get('dob'),
        gender = kwargs.get('gender'),
        address = kwargs.get('address'),
        college_name = kwargs.get('college_id')
        course_id = kwargs.get('course_id')
        start_date = kwargs.get('start_date'),
        additional_comment = kwargs.get('additional_comment'),


        Enrollment = request.env['enrollment.form']
        course = request.env['course.course'].browse(int(course_id))
        course_name = course[0].name


        enroll =Enrollment.sudo().search([('email','=',email)],limit=1)

        if enroll:
            return request.render('student_info.enrollment_submission_form',{
                'error':'The Student with this Email is Already Exists'
            })
        try:
            new_enroll = Enrollment.sudo().create({
                'name':name,
                'phone':phone,
                'email':email,
                'dob': dob[0],
                'gender':gender[0],
                'address':address[0],
                'college_name': college_name,
                'course_name':course_name,
                'start_date':start_date[0],
                'additional_comment':additional_comment[0]

            })
            partner, user = new_enroll.create_partner_and_portal_user()

            return request.render('student_info.enrollment_submission_form')
        
        except ValidationError as e:
            return request.render('student_info.enrollment_submission_form',{
                'error': e.name
            })
        
    # Route for Enrollment List on Portal 
    @http.route('/my/enrollment', type='http', auth='user', website=True) 
    def portal_my_enrollment(self):
        current_user = request.env.user
        enroll_object = request.env['enrollment.form']

        if current_user.has_group('student_info.group_supervisor'):
            enrollment = enroll_object.sudo().search([])
        else:
            enrollment = enroll_object.sudo().search([('email', '=', current_user.email)])


        return request.render('student_info.portal_enrollment',{
            'enrollment':enrollment,
        })
