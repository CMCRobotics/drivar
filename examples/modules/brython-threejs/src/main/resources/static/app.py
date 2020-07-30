import sys
    #    from drivar.Drivar import Drivar
    #    from drivar.DrivarThreejs import DrivarThreejs
from browser import document as doc
from browser import window
from javascript import JSObject,JSConstructor
import logging


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    #    drivar = DrivarThreejs()
    #    drivar.initialize()
# Expose the drivar object to current window
    #    window['drivar_turn'] = drivar.turn
    #    window['drivar_move'] = drivar.move

    #    drivar.move()
    #    drivar.turn()

    #    drivar.rotateWheels()

    #    drivar.stop()

# eval(__BRYTYHON__.py2js(src).to_js()))


THREE = window.THREE
print(THREE)

cameraC = THREE.PerspectiveCamera.new
camera = cameraC( 45, window.innerWidth / window.innerHeight, 1, 10000 )
print('ok')

controlsC = THREE.OrbitControls.new
controls = controlsC( camera )

sceneC = THREE.Scene.new
global scene
scene = sceneC()

geometryC = THREE.CubeGeometry.new
geometry = geometryC(200, 200, 200)

materialC = THREE.MeshNormalMaterial.new
material = materialC( { "color": "#ff0000", "wireframe": True } )

objectLoaderC = THREE.ObjectLoader.new;
objectLoader = objectLoaderC()
objectLoader.load("scene.json", loadedScene)

meshC = THREE.Mesh.new
mesh = meshC( geometry, material )
scene.add( mesh );

rendererC = THREE.WebGLRenderer.new
renderer = rendererC()
renderer.setSize( window.innerWidth, window.innerHeight );

camera.position.set( 0, 20, 100 )
controls.update()

doc <= renderer.domElement
renderer.render( scene, camera )

def loadedScene():
    scene = loadedScene;
    colorC = THREE.Color.new
    scene.background = colorC( 0xffffff )

def animate(i):
    # note: three.js includes requestAnimationFrame shim
    window.requestAnimationFrame( animate )
    controls.update()
    mesh.rotation.x += 0.01;
    # mesh.rotation.y += 0.02;
    renderer.render( scene, camera )

animate(0)