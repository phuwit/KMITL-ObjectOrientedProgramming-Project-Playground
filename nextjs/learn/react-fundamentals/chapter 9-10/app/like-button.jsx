'use client';

import { useState } from "react";

export default function LikeButton() {
    const [likesCount, setLikesCount] = useState(0);

    function handleLikeClick() {
        setLikesCount(likesCount + 1);
    }

    return <button onClick={handleLikeClick}>Like({likesCount})</button>
}