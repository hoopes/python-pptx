# encoding: utf-8

"""
lxml custom element classes for slide master-related XML elements.
"""

from __future__ import absolute_import

from .. import parse_xml
from ..ns import nsdecls
from ..xmlchemy import (
    BaseOxmlElement, OneAndOnlyOne, ZeroOrOne
)

class CT_NotesSlide(BaseOxmlElement):
    """
    ``<p:notes>`` element, root of a slide part
    """
    _tag_seq = ('cSld', 'clrMapOvr', )
    cSld = OneAndOnlyOne('p:cSld')
    clrMapOvr = ZeroOrOne('p:clrMapOvr', successors=_tag_seq[2:])
    del _tag_seq

    @classmethod
    def new(cls):
        """
        Return a new ``<p:sld>`` element configured as a base slide shape.
        """
        return parse_xml(cls._sld_xml())

    @property
    def spTree(self):
        """
        Return required `p:cSld/p:spTree` grandchild.
        """
        return self.cSld.spTree

    @staticmethod
    def _sld_xml():
        return (
            '<p:notes %s>\n'
            '  <p:cSld>\n'
            '    <p:spTree>\n'
            '      <p:nvGrpSpPr>\n'
            '        <p:cNvPr id="1" name=""/>\n'
            '        <p:cNvGrpSpPr/>\n'
            '        <p:nvPr/>\n'
            '      </p:nvGrpSpPr>\n'
            '      <p:grpSpPr/>\n'
            '    </p:spTree>\n'
            '  </p:cSld>\n'
            '  <p:clrMapOvr>\n'
            '    <a:masterClrMapping/>\n'
            '  </p:clrMapOvr>\n'
            '</p:notes>' % nsdecls('a', 'p', 'r')
        )
