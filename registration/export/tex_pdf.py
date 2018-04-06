import os
import latex
from django.template.loader import get_template

def pdflatex(texfile, context, pdfout):
    """
    Convert the texfile, given as a template together with the context into
    the bytestream-object pdfout
    """
    template = get_template(texfile)
    rendered = template.render(context).encode('utf8')

    # The tex file is stored for debuggign purposes
    dbgfilename = '/tmp/rendered_{}'.format(os.path.basename(texfile))
    with open(dbgfilename, 'wb') as dbgfile:
        dbgfile.write(rendered)

    tex_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'templates', 'tex')
    pdf = latex.build.build_pdf(
        rendered,
        texinputs=[tex_path, ''])
    pdf.save_to(pdfout)
