# -*- coding: utf-8 -*-

from collective.multitheme import _
from Products.Five import BrowserView
from plone import api


class folderContentsAccordian(BrowserView):

    title = _('accrodian view')

    def getDocuments(self):
        items = self.context.listFolderContents(
            contentFilter={"portal_type": "Document"}
            )
        return items

    def canEdit(self, obj):
        # import pdb;pdb.set_trace()
        try:
            current = api.user.get_current()
            perm = api.user.has_permission(
                'Modify Portal Content',
                username=current.getUserName(),
                obj=obj)
            return perm
        except Exception:
            return False
