# Permissions and Groups Setup

## Custom Permissions

The `Document` model has the following custom permissions:

- can_view: Allows viewing of documents.
- can_create: Allows creation of new documents.
- can_edit: Allows editing of documents.
- can_delete: Allows deletion of documents.

## Groups

Three groups have been created:

- **Viewers**: Can only view documents.
- **Editors**: Can view, create, and edit documents.
- **Admins**: Can perform all actions, including deleting documents.

## Permission Enforcement

Views have been updated to enforce permissions using the `@permission_required` decorator. For example, only users with the `can_edit` permission can access the document editing view.
