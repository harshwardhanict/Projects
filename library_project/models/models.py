

from odoo import models, fields, api


class library_project(models.Model):
    _name = 'library_project.library_project'
    _description = 'library_project.library_project'
    _rec_name ='book_name'


    image = fields.Binary(string="Book Image")
    book_name = fields.Char(string="Book Name")
    author = fields.Char(string="Author")
    publisher = fields.Char(string="Publisher")
    price = fields.Float(string="Price")
    genre = fields.Selection([('crime', 'Crime'), ('thrilled', 'Thrilled'), ('supernatural', 'Supernatural'), ('comedy', 'Comedy'), ('romance', 'Romance'), ('fictional', 'Fictional'),('mystery', 'Mystery'),('non-fictional', 'Non-Fictional'),('drama', 'Drama')])
    Publisher_date = fields.Date(string="Publisher Date")
    binding = fields.Selection(
        [('paperback', 'PaperBack'), ('hardcover', 'HardCover')])
    language = fields.Selection(
        [('english', 'English'), ('hindi', 'Hindi'), ('marathi', 'Marathi'), ('gujarati', 'Gujarati'), ('french', 'French'), ('arabic', 'Arabic'),('spanish', 'Spanish')])
    description = fields.Text(string="Description")
    Rating = fields.Selection(
        [('0', 'Give The Rating'), ('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')])

