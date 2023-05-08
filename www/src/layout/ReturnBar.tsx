import Root from '@/components/tunnels/Root';
import React, { FC } from 'react';
import { useNavigate } from 'react-router-dom';

const ReturnBar: FC = () => {
	const navigator = useNavigate();

	return (
		<Root.In>
			<div className="absolute top-0 left-0 w-screen flex justify-center content-center z-10">
				<h1
					onClick={() => navigator('/')}
					className="text-white hover:cursor-pointer"
				>
					Return
				</h1>
			</div>
		</Root.In>
	);
};

export default ReturnBar;
