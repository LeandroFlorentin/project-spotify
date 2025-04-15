from db import get_session
from sqlmodel import select
from models import Song, Favourites
from fastapi import HTTPException
from typing import List, Dict, Any


async def add_favourite(body_dict, user_data):
    try:
        session = get_session()

        fav_statement = select(Favourites).where(
            Favourites.idspotify == body_dict["idspotify"],
            Favourites.iduser == user_data["id"],
        )
        existing_fav = session.exec(fav_statement).first()

        if existing_fav:
            raise HTTPException(
                status_code=400, detail="Esta canción ya está en tus favoritos"
            )

        song_statement = select(Song).where(Song.idspotify == body_dict["idspotify"])
        song = session.exec(song_statement).first()

        if not song:
            new_song = Song(**body_dict)
            session.add(new_song)
            session.commit()
            session.refresh(new_song)

        new_favourite = Favourites(
            iduser=user_data["id"],
            idspotify=body_dict["idspotify"],
        )
        session.add(new_favourite)
        session.commit()
        session.refresh(new_favourite)
        return {"message": "Favourite added successfully"}
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_favourites(iduser: int) -> List[Dict[str, Any]]:
    try:
        session = get_session()
        statement = (
            select(Song, Favourites)
            .join(Favourites, Favourites.idspotify == Song.idspotify)
            .where(Favourites.iduser == iduser)
        )
        results = session.exec(statement).all()

        return [
            {
                "idfavourite": favourite.id,
                "idsong": song.idsong,
                "idspotify": song.idspotify,
                "name": song.title,
                "artist": song.artist,
                "album": song.album,
                "year": song.year,
                "url_image": song.url_image,
                "created_at": song.created_at,
            }
            for song, favourite in results
        ]
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def delete_favourite(idfavourite: int):
    try:
        session = get_session()
        statement = select(Favourites).where(Favourites.id == idfavourite)
        favourite = session.exec(statement).first()
        if not favourite:
            raise HTTPException(status_code=404, detail="Favourite not found")
        session.delete(favourite)
        session.commit()
        return {"message": "Favourite deleted successfully"}
    except HTTPException as he:
        raise he
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
