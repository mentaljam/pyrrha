/* -*- coding: utf-8-unix -*-
 *
 * Pyrrha, a cute pandora client.
 * Copyright (C) 2015 Core Comic <core.comic@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

import QtQuick 2.0


ListModel{
    id: songModel

    function loadSongs(doStart) {
        doStart = typeof doStart !== 'undefined' ? doStart : false;

        py.call('pyrrha.get_playlist', [], function() {
            py.call('pyrrha.get_song_list', [], function(result) {
                songModel.clear();
                for (var i=0; i<result.length; i++) {
                    songModel.append(result[i]);
                }
                player.song = songModel.get(player.songIndex);
                console.log('SongList Updated...');
                if (doStart) {
                    player.playbackSong(player.song.audioURL);
                }
            })
        })
    }

    function hasSongs() {
        return songModel.count > 0
    }
}
