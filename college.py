# -*- coding: utf-8 -*-
##############################################################################
#
#    Qt College: The Free Campus and Student Information System
#    Copyright (C) 2012-2013  Qtcollege <admin@qtcollege.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################

from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval, Bool, Not, Get
from trytond.transaction import Transaction
from trytond.pool import Pool



class Teacher(ModelSQL, ModelView):
    'Teacher'
    _name = 'qtcollege.teacher'

    name = fields.Many2One('party.party', 'Teacher', required=True,
        domain=[
            ('is_teacher', '=', True),
            ('is_person', '=', True),
            ],
        help='Teacher\'s Name, from the partner list')
    institution = fields.Many2One('party.party', 'institution',
        domain=[('is_institution', '=', True)],
        help='Instituion where she/he works')
    code = fields.Char('ID', help='Teacher ID')
    info = fields.Text('Extra info')


Teacher()



class Subject(ModelSQL, ModelView):
    'Subjects'
    _name = 'qtcollege.subject'
    _rec_name = 'name'
    #Module: moduleID Integer (One2Many? classID) moduleTitle Char creditHours Integer moduleDescription Text
    credit_hours = fields.Char('Credit Hours')
    name = fields.Many2One('product.product', 'Product', required=True,
        domain=[('is_subject', '=', True)],
        help='Product Name')
    category = fields.Many2One('product.category', 'Category',
        select=True)
    notes = fields.Text('Subject Description')

    
Subject()


class PartyStudent(ModelSQL, ModelView):
    'Party'
    _name = 'party.party'

    alias = fields.Char('Alias', help='Common name that the Party is reffered')
    is_person = fields.Boolean('Person',
        help='Check if the party is a person.')
    is_student = fields.Boolean('Student',
        help='Check if the party is a student')
    is_teacher = fields.Boolean('Teacher',
        help='Check if the party is a Teacher')
    is_institution = fields.Boolean('Institution',
        help='Check if the party is a Educational Center')
    lastname = fields.Char('Last Name', help='Last Name')
    citizenship = fields.Many2One('country.country','Citizenship', help='Country of Citizenship')
    residence = fields.Many2One('country.country','Country of Residence', help='Country of Residence')
    internal_user = fields.Many2One('res.user', 'Internal User',
        help='In QT College users like teachers and staff can  logins. When the'
        ' party is a teacher or a educational center or Student.',
        states={
            'invisible': Not(Bool(Eval('is_teacher'))),
            'required': Bool(Eval('is_teacher')),
            }
        )
   
PartyStudent()



class Product(ModelSQL, ModelView):
    'Product'
    _name = 'product.product'

    is_subject = fields.Boolean('subject',
        help='Check if the product is a Subject avialable for purchase')
    
Product()




class StudentData(ModelSQL, ModelView):
    'Student related information'
    _name = 'qtcollege.student'

    name = fields.Many2One('party.party', 'student', required=True,
        domain=[
            ('is_student', '=', True),
            ('is_person', '=', True),
            ],
        help='student Name')
    lastname = fields.Function(fields.Char('Lastname'),
        'get_student_lastname', searcher='search_student_lastname')
    ssn = fields.Function(fields.Char('SSN'),
        'get_student_ssn', searcher='search_student_ssn')
    identification_code = fields.Char('ID', readonly=True,
        help='student Identifier provided by the University.Is not the'
        ' Social Security Number')
    current_address = fields.Many2One('party.address', 'Address',
        domain=[('party', '=', Eval('name'))],
        depends=['name'],
        help='Contact information. You may choose from the different contacts'
        ' and addresses this student has.')
    photo = fields.Binary('Picture')
    dob = fields.Date('DoB', help='Date of Birth')
    #age = fields.Function(fields.Char('Age'), 'student_age')
    sex = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ], 'Sex', required=True)
    marital_status = fields.Selection([
        (None, ''),
        ('s', 'Single'),
        ('m', 'Married'),
        ('c', 'Concubinage'),
        ('w', 'Widowed'),
        ('d', 'Divorced'),
        ('x', 'Separated'),
        ], 'Marital Status', sort=False)

    #ethnic_group = fields.Many2One('qtcollege.ethnicity', 'Ethnic group')

    subjects = fields.One2Many('qtcollege.subject', 'name',
        'Subjects')

    general_info = fields.Text('General Information',
        help='General information about the patient')
    
  

StudentData()

