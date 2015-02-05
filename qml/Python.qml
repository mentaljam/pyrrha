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
import io.thp.pyotherside 1.3


Python {
    id: py

    property string progname: 'pyrrha'
    property bool ready: false
    property bool refreshing: false
    property string version

    signal connected()

    Component.onCompleted: {
        // Configure Signal Handlers for PyOtherSide
        setHandler('connected', connected)

        // Add path for Python module
        addImportPath(Qt.resolvedUrl("../pyrrha"));

        // Load the Python side of things
        importModule("pyrrha", function() {
            py.call("pyrrha.init", [], function() {
            py.ready = true;
            });
        });
    }


    onConnected: {
        console.log('Successfully Connected!')
        pandoraSession.isConnected = true;
    }

    onReceived: {
        console.log('unhandled message: ' + data);
    }

    onError: {
        console.log('Python failure: ' + traceback);
    }
}