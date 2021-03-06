##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Ross(CMakePackage):
    """Rensselaer's Optimistic Simulation System"""

    homepage = "http://carothersc.github.io/ROSS/"
    git = "https://github.com/carothersc/ROSS.git"

    version('master')

    depends_on('mpi')

    def cmake_args(self):
        if 'x86_64' not in spec.architecture:
            raise InstallError(
                'This package currently only builds on x86_64 architectures')

        args = ["-DBUILD_SHARED_LIBS=ON",
                "-DARCH=x86_64",
                "-DCMAKE_C_COMPILER=%s" % self.spec['mpi'].mpicc,
                "-DCMAKE_CXX_COMPILER=%s" % self.spec['mpi'].mpicxx]
        return args
