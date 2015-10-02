# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1443802885.9030464
_enable_loop = True
_template_filename = 'themes/monospace/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        _link = context.get('_link', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        index_teasers = context.get('index_teasers', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        _link = context.get('_link', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        index_teasers = context.get('index_teasers', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for post in posts:
            __M_writer('        <div class="postbox">\n        <h1><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('">')
            __M_writer(str(post.title()))
            __M_writer('</a></h1>\n            <div class="meta" style="background-color: rgb(234, 234, 234); ">\n                <span class="authordate">\n                    ')
            __M_writer(str(messages("Posted:")))
            __M_writer(' <time class="published" datetime="')
            __M_writer(str(post.date.isoformat()))
            __M_writer('">')
            __M_writer(str(post.formatted_date(date_format)))
            __M_writer('</time>\n                </span>\n                <br>\n                <span class="tags">Tags:&nbsp;\n')
            if post.tags:
                for tag in post.tags:
                    __M_writer('                            <a class="tag" href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('"><span>')
                    __M_writer(str(tag))
                    __M_writer('</span></a>\n')
            __M_writer('                </span>\n            </div>\n        ')
            __M_writer(str(post.text(teaser_only=index_teasers)))
            __M_writer('\n')
            if not post.meta('nocomments'):
                __M_writer('            ')
                __M_writer(str(comments.comment_link(post.permalink(), post.base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n')
        __M_writer('    ')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n\t')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.tmpl", "source_encoding": "utf-8", "filename": "themes/monospace/templates/index.tmpl", "line_map": {"23": 3, "26": 2, "32": 0, "46": 2, "47": 3, "48": 4, "53": 31, "59": 5, "72": 5, "73": 6, "74": 7, "75": 8, "76": 8, "77": 8, "78": 8, "79": 11, "80": 11, "81": 11, "82": 11, "83": 11, "84": 11, "85": 15, "86": 16, "87": 17, "88": 17, "89": 17, "90": 17, "91": 17, "92": 20, "93": 22, "94": 22, "95": 23, "96": 24, "97": 24, "98": 24, "99": 26, "100": 28, "101": 28, "102": 28, "103": 29, "104": 29, "105": 30, "106": 30, "112": 106}}
__M_END_METADATA
"""
