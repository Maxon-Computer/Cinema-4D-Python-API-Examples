// Contains the UI description of the Olicenseablecube object.
CONTAINER Olicenseablecube
{
	NAME Olicenseablecube;
	INCLUDE Obase;

	GROUP ID_OBJECTPROPERTIES
	{
		// The interface for the three dimension parameters of the cube.
		REAL PY_LICENSABLE_CUBE_HEIGHT { UNIT METER; MIN 0.0; }
		REAL PY_LICENSABLE_CUBE_WIDTH { UNIT METER; MIN 0.0; }
		REAL PY_LICENSABLE_CUBE_DEPTH { UNIT METER; MIN 0.0; }

		SEPARATOR { }
		
		// A button to get a license for this object.
		BUTTON PY_LICENSABLE_GET_LICENSE { }
	}
}
