# -*- coding: utf-8 -*-

from collective.multitheme import _
from Products.Five import BrowserView


class folderContentsAccordian(BrowserView):

    title = _('accrodian view')

    def getDocuments(self):
        items = self.context.listFolderContents(
            contentFilter={"portal_type": "Document"}
            )
        return items
