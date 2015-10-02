# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1443802885.4719713
_enable_loop = True
_template_filename = 'themes/monospace/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        pheader = _mako_get_namespace(context, 'pheader')
        def content():
            return render_content(context._locals(__M_locals))
        _link = context.get('_link', UNDEFINED)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        helper = _mako_get_namespace(context, 'helper')
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        pheader = _mako_get_namespace(context, 'pheader')
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="post">\n    ')
        __M_writer(str(pheader.html_title()))
        __M_writer('\n        <div class="meta" style="background-color: rgb(234, 234, 234); ">\n        <span class="authordate">\n            ')
        __M_writer(str(messages("Posted:")))
        __M_writer(' <time class="published" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time>\n')
        if not post.meta('password'):
            __M_writer('               [<a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>]\n')
        __M_writer('        </span>\n        <br>\n')
        if post.tags:
            __M_writer('                <span class="tags">')
            __M_writer(str(messages("Tags")))
            __M_writer(':&nbsp;\n')
            for tag in post.tags:
                __M_writer('                    <a class="tag" href="')
                __M_writer(str(_link('tag', tag)))
                __M_writer('"><span>')
                __M_writer(str(tag))
                __M_writer('</span></a>\n')
            __M_writer('                </span>\n                <br>\n')
        __M_writer('        <span class="authordate">\n            ')
        __M_writer(str(pheader.html_translations(post)))
        __M_writer('\n        </span>\n        </div>\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n')
        if not post.meta('nocomments'):
            __M_writer('        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer('\n')
        __M_writer('    ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "post.tmpl", "source_encoding": "utf-8", "filename": "themes/monospace/templates/post.tmpl", "line_map": {"128": 26, "129": 28, "130": 31, "131": 32, "132": 32, "133": 35, "134": 35, "135": 36, "136": 36, "137": 37, "138": 38, "139": 38, "140": 38, "141": 40, "142": 40, "143": 40, "149": 143, "23": 4, "26": 3, "29": 2, "35": 0, "51": 2, "52": 3, "53": 4, "54": 5, "59": 11, "64": 42, "70": 6, "78": 6, "79": 7, "80": 7, "81": 8, "82": 9, "83": 9, "84": 9, "90": 12, "103": 12, "104": 14, "105": 14, "106": 17, "107": 17, "108": 17, "109": 17, "110": 17, "111": 17, "112": 18, "113": 19, "114": 19, "115": 19, "116": 19, "117": 19, "118": 21, "119": 23, "120": 24, "121": 24, "122": 24, "123": 25, "124": 26, "125": 26, "126": 26, "127": 26}}
__M_END_METADATA
"""
