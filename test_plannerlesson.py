# test_plannerlesson.py
"""
Tests for PlannerLesson module.
"""

import unittest
from plannerlesson import PlannerLesson

class TestPlannerLesson(unittest.TestCase):
    """Test cases for PlannerLesson class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PlannerLesson()
        self.assertIsInstance(instance, PlannerLesson)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PlannerLesson()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
