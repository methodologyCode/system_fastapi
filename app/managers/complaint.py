from db import database
from models import complaint, RoleType, State


class ComplaintManager:
    @staticmethod
    async def get_complaints(user):
        query = complaint.select()

        if user["role"] == RoleType.complainer:
            query = query.where(complaint.c.complainer_id == user["id"])
        elif user["role"] == RoleType.approver:
            query = query.where(complaint.c.status == State.pending)

        return await database.fetch_all(query)
    
    @staticmethod
    async def create_complaint(complaint_data, user):
        complaint_data["complainer_id"] = user["id"]
        id_ = await database.execute(complaint.insert().values(complaint_data))
        query = complaint.select().where(complaint.c.id == id_)
        return await database.fetch_one(query)
    
    @staticmethod
    async def delete(compl_id):
        await database.execute(complaint.delete().where(complaint.c.id == compl_id))

    @staticmethod
    async def approve(id_):
        query = complaint.update().where(complaint.c.id == id_).values(status=State.approved)
        await database.execute(query)

    @staticmethod
    async def reject(id_):
        query = complaint.update().where(complaint.c.id == id_).values(status=State.rejected)
        await database.execute(query)