from typing import Optional
from dataclasses import dataclass

from bot import fym


@dataclass
class Result:
    nsfw_hentai: int
    created_at: str
    source_page_url: str
    meme_type: str
    meme_file_size: int
    nsfw_neutral: int
    source_site: str
    image_path: str
    file_hash: str
    updated_at: str
    thumbnail: Optional[str]
    
    @classmethod
    def from_json(cls, data: dict) -> "Result":
        nsfw_hentai = data.get("nsfw_hentai")
        created_at = data.get("created_at")
        source_page_url = data.get("source_page_url")
        meme_type = data.get("type")
        meme_file_size = data.get("meme_file_size")
        nsfw_neutral = data.get("nsfw_neutral")
        source_site = data.get("source_site")
        image_path = data.get("image_path")
        file_hash = data.get("file_hash")
        updated_at = data.get("updated_at")
        thumbnail = data.get("thumbnail")
        return cls(
            nsfw_hentai=nsfw_hentai,
            image_path=image_path,
            created_at=created_at,
            source_page_url=source_page_url,
            meme_type=meme_type,
            meme_file_size=meme_file_size,
            nsfw_neutral=nsfw_neutral,
            source_site=source_site,
            file_hash=file_hash,
            updated_at=updated_at,
            thumbnail=thumbnail
        )
    
    @property
    def image_path_url(self) -> str:
        return f"{fym.CDN_URL}/{self.image_path}"
    @property
    def thumbnail_url(self) -> str:
        return f"{fym.CDN_URL}/thumb/{self.thumbnail}" if self.thumbnail else None