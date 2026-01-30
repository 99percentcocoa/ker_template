from dataclasses import dataclass, field
from typing import Dict, List, Optional
from pathlib import Path

import cv2
import numpy as np
from questions import questions

@dataclass
class SheetMeta:
    """Metadata for a sheet in a document."""
    sheet_id: int = 0
    student_name: str = None
    student_grade: int = None
    student_school: str = None
    student_tfi_id: str = None
    template_name: str = None

    def __str__(self):
        return f"Survey ID {self.sheet_id} - Name: {self.student_name}, Grade: {self.student_grade}, School: {self.student_school}, TFI ID: {self.student_tfi_id}"
    
@dataclass
class InputImageMeta:
    """Metadata for an input image."""
    image_path: Optional[Path | str] = None
    image_array: Optional[np.ndarray] = None
    
    def __post_init__(self):
        """Validate that either image_path or image_array is provided."""
        if self.image_path is None and self.image_array is None:
            raise ValueError("Either image_path or image_array must be provided")
        if self.image_path is not None and self.image_array is not None:
            raise ValueError("Only one of image_path or image_array should be provided")
        
        # If image_path is provided and image_array is None, load the image
        if self.image_path is not None and self.image_array is None:
            self.load_bytes(str(self.image_path))
    
    def load_bytes(self, image_path: str) -> bool:
        """Load the image from filepath using cv2.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            True if image loaded successfully, False otherwise
        """
        self.image_path = image_path
        self.image_array = cv2.imread(image_path)
        return self.image_array is not None