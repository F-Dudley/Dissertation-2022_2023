import { type FC } from 'react';
import { useParams } from 'react-router-dom';
import PCDViewer from '@/components/canvas/PCDViewer';
import View from '@/components/canvas/View';
import Root from '@/components/tunnels/Root';
import { SCANNING_TECHNIQUES } from '@/data/constants';

const SphereTechniqueID: FC = () => {
    const { techniqueID } = useParams()

    if (!SCANNING_TECHNIQUES.includes(techniqueID as string) || !techniqueID) {
      console.log(`TechniqueID: ${techniqueID} is not a valid technique ID.`)
      return <Root.In><h1>404</h1></Root.In>
    }

    const cloudDir = `/clouds/${techniqueID}/sphere.ply`;

    return (
        <View>
            <PCDViewer 
                dir={cloudDir} 
                loading ={
                  <div>
                    <h1>LOADING</h1>
                  </div>
                }
            />
        </View>
    )
}

export default SphereTechniqueID