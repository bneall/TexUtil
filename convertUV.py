#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================================
#UV Notation Conversion Tool
#Copyright (C) 2015  Ben Neall

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or 
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#============================================================

import re

def convertUV(uvTile=None, UDIM=None, UV=None, output=None):
    '''This function allows for conversion between UV multiple notations
    Example Usage:  convertUV(UDIM=1005, output="uvTile")
    
    Parameters:
    
        uvTile takes:
        str : "u1_v1"
        
        UDIM takes:
        str : "1001"
        int : 1001
        
        UV takes:
        str : "1,1"
        list of str : ["1", "1"]
        list of int : [1, 1]
        
    '''

    #--------------------------------------------------------------------------------
    # Import
    #--------------------------------------------------------------------------------
    
    #------- Process UDIM -------
    if UDIM:
        try:
            u, v = validateUDIM(UDIM)
        except:
            raise Exception('"%s" is an Invalid data type for UDIM' % UDIM)
            return

    #------- Process uvTile -------
    if uvTile:
        try:
            u, v = validateTile(uvTile)
        except:
            raise Exception('"%s" is an Invalid data type for uvTile' % uvTile)
            return

    #------- Process UV -------
    if UV:
        try:
            u, v = validateUV(UV)
        except:
            raise Exception('"%s" is an Invalid data type for UV' % UV)
            return

    #--------------------------------------------------------------------------------
    # Export
    #--------------------------------------------------------------------------------

    #------- Export UDIM -------
    if output == "UDIM":
        uvExport = 1000 + (u+1) + (v*10)
        return uvExport

    #------- Export uvTile -------
    if output == "uvTile":
        uvExport = "u%s_v%s" % (u+1, v+1)
        return uvExport
    
    #------- Export UV -------
    if output == "UV":
        uvExport = (u, v)
        return uvExport


#Validate UV Types
#------------------------------------------------------------------------------------

#-- UDIM
#----------------------------------------------------------------
def validateUDIM(udim):
    if type(udim) is str or type(udim) is int:
        if len(str(udim)) == 4: 
            try:
                udim = int(udim)
                u = ( int(udim) - 1001 ) % 10
                v = ( int(udim) - 1000 ) / 10
                return [u, v]
            except Exception as e:
                raise Exception(e)
                return False
        else:
            return False

#-- uvTile
#----------------------------------------------------------------
def validateTile(uvTile):
    if type(uvTile) is str:
        try:
            u, v = [ ''.join(re.findall(r'\d+', i))  for i in uvTile.split("_") ]
            u, v = [ int(i) - 1 for i in [u, v] ]
            return [u, v]
        except Exception as e:
            raise Exception(e)
            return False
    else:
        return False

#-- UV
#----------------------------------------------------------------
def validateUV(uv):
    if type(uv) is list:
        try:
            u, v  = [ int(i) for i in uv ]
            return [u, v]
        except Exception as e:
            raise Exception(e)
            return False
    elif type(uv) is str:
        try:
            u, v = [ int(i) for i in uv.split(",") ]
            return [u, v]
        except Exception as e:
            raise Exception(e)
            return False
    else:
        return False
